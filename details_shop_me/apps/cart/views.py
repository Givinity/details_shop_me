from urllib import request

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from .models import Basket
from details_shop_me.apps.detailapp.urls import DataMixin
from details_shop_me.apps.detailapp.models import Details


class Cart_user(DataMixin, LoginRequiredMixin, ListView):
    """
    Корзина для покупок
    """
    template_name = 'cart/cart.html'
    login_url = reverse_lazy('login')
    context_object_name = 'cart_items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Корзина')
        context['my_price'] = sum([item.product.price * item.quantity for item in self.get_queryset()])
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user)


def cart_add(request, product_id):
    product = Details.objects.get(id=product_id)
    carts = Basket.objects.filter(user=request.user, product=product)

    if not carts.exists():
        Basket.objects.create(user=request.user, product=product,
                              quantity=1)
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def cart_del(request, cart_id):
    cart = Basket.objects.get(id=cart_id)
    cart.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

