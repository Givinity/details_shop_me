from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .utils import DataMixin
from .models import Details
from django.views.generic import ListView, TemplateView

menu = [
    {'title': 'Главная', "url_name": 'index'},
    {'title': 'Каталог', "url_name": 'catalog'},
    {'title': 'О нас', "url_name": 'info'},
    {'title': 'Контакты', "url_name": 'contacts'},
]


class IndexView(DataMixin, ListView):
    """
    Главная страница
    """
    model = Details
    template_name = 'pages/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Details.objects.filter(published_or_not=True)


class DetailsCategory(DataMixin, ListView):
    """"
        Отображение категорий
    """
    model = Details
    template_name = 'pages/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Details.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                      published_or_not=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' +
                                            str(context['posts'][0].cat))
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class Catalog(TemplateView):
    template_name = 'pages/catalog.html'
    allow_empty = False


def info(request):
    return render(request, 'pages/info.html')


def contacts(request):
    return render(request, 'pages/contacts.html')


class Cart(LoginRequiredMixin, TemplateView):
    template_name = 'pages/cart.html'
    login_url = reverse_lazy('index')
    raise_exception = True

