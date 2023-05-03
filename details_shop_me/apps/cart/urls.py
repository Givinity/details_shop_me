from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', Cart_user.as_view(), name='cart'),
]