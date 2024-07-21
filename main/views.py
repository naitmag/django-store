from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpRequest:
    context = {

    }

    return render(request, 'main/index.html', context)


def about(request: HttpRequest) -> HttpRequest:
    return HttpResponse('about')
