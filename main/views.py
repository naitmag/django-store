from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Главная'
        context['content'] = 'Магазин мебели HOME'
        return context


# def index(request: HttpRequest) -> HttpResponse:
#     goods = Products.objects.all()
#
#     context = {
#         'title': 'Home - Главная',
#         'content': 'Магазин мебели HOME',
#         'goods': goods
#     }
#
#     return render(request, 'main/index.html', context)

class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - О нас'
        context['content'] = 'О нас'
        context['text_on_page'] = 'Это текст про наш магазин'
        return context

# def about(request: HttpRequest) -> HttpRequest:
#     context = {
#         'title': 'Home - О нас',
#         'content': 'О нас',
#         'text_on_page': 'Это текст про наш магазин'
#     }
#
#     return render(request, 'main/about.html', context)
