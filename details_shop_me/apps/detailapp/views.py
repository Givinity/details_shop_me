from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import RegisterUserForm, LoginUserForm
from .utils import DataMixin
from .models import Details
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, TemplateView, CreateView, DetailView

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


class ShowDetail(DataMixin, DetailView):
    """
    Отображение информации о детали
    """
    model = Details
    template_name = 'pages/detail-info.html'
    slug_url_kwarg = 'detail_slug'
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['detail'])
        return dict(list(context.items()) + list(c_def.items()))


def info(request):
    return render(request, 'pages/info.html')


def contacts(request):
    return render(request, 'pages/contacts.html')


class RegisterUser(DataMixin, CreateView):
    """
    Регистрация пользователей
    """
    form_class = RegisterUserForm
    template_name = 'pages/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    """
    Авторизация пользователей
    """
    form_class = LoginUserForm
    template_name = 'pages/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')
