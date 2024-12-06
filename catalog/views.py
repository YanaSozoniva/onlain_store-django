from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Product


def home(request):
    # Получаем последние 5 созданных продуктов
    latest_products = Product.objects.order_by('-created_at')[:5]

    # Выводим продукты в консоль
    for product in latest_products:
        print(product)

    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get("phone")
        print(f'POST-запрос от пользователя: {name}, тел: {phone}, сообщение: {message}')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html')
