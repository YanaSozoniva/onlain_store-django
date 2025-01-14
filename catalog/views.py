from catalog.forms import ProductForm
from django.urls import reverse_lazy, reverse
from catalog.models import Product, Contact
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView


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


class CatalogCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class CatalogUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class CatalogDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
