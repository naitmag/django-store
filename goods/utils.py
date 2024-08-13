from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.shortcuts import get_list_or_404
from django.db.models import Q

from goods.models import Products


def query_search(query: str):
    if query.isdigit() and len(query) < 5:
        return get_list_or_404(Products.objects.filter(id=int(query)))

    vector = SearchVector('name', 'description')
    query = SearchQuery(query)
    return get_list_or_404(
        Products.objects.annotate(rank=SearchRank(vector, query)).order_by("-rank")
    )

    # keywords = [word for word in query.split() if len(word) > 2]
    #
    # q_objects = Q()
    #
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
    #
    # return Products.objects.filter(q_objects)
