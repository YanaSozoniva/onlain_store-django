from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Product, Contact
from catalog.forms import AddProduct
# from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, TemplateView


class CatalogListViews(ListView):
    model = Product
    template_name = 'product_list.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.paginate_by:
            paginator = context['paginator']
            context['is_paginated'] = paginator.num_pages > 1
        return context


# def products_list(request):
#     # Получаем последние 5 созданных продуктов
#     # latest_products = Product.objects.order_by('-created_at')[:5]
#     products = Product.objects.all()
#     # постраничные вывод списка товаров по 3 на одной странице
#     paginator = Paginator(products, 3)
#     # Получаем номер страницы
#     page_number = request.GET.get('page')
#     product_page = paginator.get_page(page_number)
#     context = {"product_page": product_page}
#     # Выводим продукты в консоль
#     # for product in latest_products:
#     #     print(product)
#
#     return render(request, 'catalog/products_list.html', context)

class ContactViews(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            message = self.request.POST.get('message')
            phone = self.request.POST.get("phone")
            print(f'POST-запрос от пользователя: {name}, тел: {phone}, сообщение: {message}')
        context_data['contact'] = Contact.objects.all()[0]
        return context_data

# def contacts(request):
#     contact = Contact.objects.all()
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#         phone = request.POST.get("phone")
#         print(f'POST-запрос от пользователя: {name}, тел: {phone}, сообщение: {message}')
#         return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
#     return render(request, 'catalog/contacts.html', {'contact': contact})


class CatalogDetailViews(DetailView):
    model = Product


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'catalog/product_detail.html', context)


def add_product(request):
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Сохранить модель в базе данных
            return redirect('/')  # Перенаправить на другую страницу
    else:
        form = AddProduct()

    return render(request, 'catalog/add_product.html', {'form': form})
