from django.shortcuts import render
from goods.models import Products, Categories


def catalog(request):
    categories = Categories.objects.all()
    goods = Products.objects.all()

    context = {
        'title': 'Home - Каталог',
        'categories': categories,
        'goods': goods
    }

    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')
