from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.core.cache import cache

from catalog.forms import ProductForm
from django.urls import reverse_lazy, reverse
from catalog.models import Product, Contact, Category
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView, View
from catalog.services import get_products_by_category


class CategoryListViews(ListView):
    model = Category
    template_name = "category_list.html"


class CategoryProductsDetailView(DetailView):
    model = Category
    template_name = "catalog/product_category.html"

    def get_context_data(self, **kwargs):
        # Получаем стандартный контекст данных из родительского класса
        context = super().get_context_data(**kwargs)
        # Получаем ID категории из объекта
        category = self.object.id
        context['products_category'] = get_products_by_category(category)
        return context


class UnpublishProductView(LoginRequiredMixin, View):

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm("catalog.can_unpublish_product"):
            raise PermissionDenied("У вас нет права на отмену публикации продукции")

        product.is_published = False
        product.save()

        return redirect("catalog:product_detail", pk=pk)


class CatalogListViews(ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 3

    def get_queryset(self):
        queryset = cache.get('product_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('product_queryset', queryset, 60 * 10)  # Кешируем данные на 10 минут
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.paginate_by:
            paginator = context["paginator"]
            context["is_paginated"] = paginator.num_pages > 1
        return context


class ContactViews(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.request.method == "POST":
            name = self.request.POST.get("name")
            message = self.request.POST.get("message")
            phone = self.request.POST.get("phone")
            print(f"POST-запрос от пользователя: {name}, тел: {phone}, сообщение: {message}")
        context_data["contact"] = Contact.objects.all()[0]
        return context_data


class CatalogDetailViews(DetailView):
    model = Product


class CatalogCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class CatalogUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_object(self,  queryset=None):
        product = super().get_object(queryset)
        user = self.request.user

        if product.owner != user:
            raise PermissionDenied

        return product


class CatalogDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self,  queryset=None):
        product = super().get_object(queryset)
        user = self.request.user

        if product.owner != user and not user.has_perm('catalog.delete_product'):
            raise PermissionDenied

        return product
