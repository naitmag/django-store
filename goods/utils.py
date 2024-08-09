from django.shortcuts import get_list_or_404

from goods.models import Products


def query_search(query: str):
    if query.isdigit() and len(query) <5:
        return get_list_or_404(Products.objects.filter(id=int(query)))

    return get_list_or_404(Products.objects.filter(name__icontains=query))

