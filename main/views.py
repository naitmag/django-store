from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Home - Main')
        context['content'] = _('Furniture store HOME')
        return context


# TODO strings config
class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Home - About us')
        context['content'] = _('About us')
        context['text_on_page'] = _('Some text here')
        return context

