from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }

    return render(request, 'main/index.html', context)


def about(request: HttpRequest) -> HttpRequest:
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Это текст про наш магазин'
    }

    return render(request, 'main/about.html', context)
