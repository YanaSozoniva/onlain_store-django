from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect


from catalog.forms import ProductForm, ProductModeratorForm
from django.urls import reverse_lazy, reverse
from catalog.models import Product, Contact
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView, View


class UnpublishProductView(LoginRequiredMixin, View):

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied("У вас нет права на отмену публикации продукции")

        product.is_published = False
        product.save()

        return redirect('catalog:product_detail', pk=pk)


class CatalogListViews(ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 3

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


class CatalogUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    # def get_form_class(self):
    #     user = self.request.user
    #     if user == self.object.owner:
    #         return ProductForm
    #     if user.has_perm('catalog.catalog.can_unpublish_product'):
    #         return ProductModeratorForm("У вас нет прав для отмены публикации продукта.")
    #     raise PermissionDenied


class CatalogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    permission_required = 'catalog.delete_product'


