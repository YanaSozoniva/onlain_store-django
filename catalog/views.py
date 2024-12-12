from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Contact


def products_list(request):
    # Получаем последние 5 созданных продуктов
    # latest_products = Product.objects.order_by('-created_at')[:5]
    latest_products = Product.objects.all()
    context = {'products': latest_products}
    # Выводим продукты в консоль
    # for product in latest_products:
    #     print(product)

    return render(request, 'catalog/products_list.html', context)


def contacts(request):
    contact = Contact.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get("phone")
        print(f'POST-запрос от пользователя: {name}, тел: {phone}, сообщение: {message}')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html', {'contact': contact})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)
