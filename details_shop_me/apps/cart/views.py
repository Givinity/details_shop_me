from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy


class Cart_user(LoginRequiredMixin, TemplateView):
    """
    Корзина для покупок
    """
    template_name = 'cart/cart.html'
    login_url = reverse_lazy('login')
