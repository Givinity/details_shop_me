from django.shortcuts import render
from .utils import *
from .models import *
from django.views.generic import ListView
# Create your views here.


menu = [
        {'title': 'Главная', "url_name": 'index'},
        {'title': 'Каталог', "url_name": 'catalog'},
        {'title': 'О нас', "url_name": 'info'},
        {'title': 'Контакты', "url_name": 'contacts'},
    ]
# def index(request):
#     menu = [
#         {'title': 'Главная', "url_name": 'index'},
#         {'title': 'Каталог', "url_name": 'catalog'},
#         {'title': 'О нас', "url_name": 'info'},
#         {'title': 'Контакты', "url_name": 'contacts'},
#     ]
#
#     return render(request, 'pages/index.html', {'menu': menu})


class IndexView(DataMixin, ListView):
    """
    Главная страница
    """
    model = Details
    template_name = 'pages/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Details.objects.filter(published_or_not=True)
def catalog(request):
    return render(request, 'pages/catalog.html')

def info(request):
    return render(request, 'pages/info.html')

def contacts(request):
    return render(request, 'pages/contacts.html')

def cart(request):
    return render(request, 'pages/cart.html')
