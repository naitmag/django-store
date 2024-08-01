from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from goods.models import Categories, Products


def index(request: HttpRequest) -> HttpResponse:
    categories = Categories.objects.all()
    goods = Products.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories,
        'goods': goods
    }

    return render(request, 'main/index.html', context)


def about(request: HttpRequest) -> HttpRequest:
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Это текст про наш магазин'
    }

    return render(request, 'main/about.html', context)
