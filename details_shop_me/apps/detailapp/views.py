from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .forms import RegisterUserForm, LoginUserForm
from .serializers import DetailsSerializer
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


class Search(DataMixin, ListView):
    """
    Поиск по товарам
    """
    template_name = 'pages/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Details.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        c_def = self.get_user_context(title='Поиск - ' +
                                            str(context['q']))
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# class ListDetailsAPI(generics.ListAPIView):
#     queryset = Details.objects.all()
#     serializer_class = ListDetailsSerializer

class ListAPIDetails(generics.ListCreateAPIView):
    """
    Create and view model in JSON data
    """
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer

class UpdateAPIDetails(generics.UpdateAPIView):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer

class ViewAPIDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer

# class ListDetailsAPI(APIView):
#     def get(self, request):
#         w = Details.objects.all()
#         return Response({'posts': DetailsSerializer(w,
#                                                     many=True).data})
#
#     def post(self, request):
#         serializer = DetailsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error':'Method PUT not allowed'})
#
#         try:
#             instance = Details.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists'})
#
#         serializer = DetailsSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#
#         try:
#             instance = Details.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists'})
#
#         instance.delete()
#         return Response({'post': 'delete post '+str(pk)})