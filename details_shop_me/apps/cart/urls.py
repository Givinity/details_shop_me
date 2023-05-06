from django.urls import path
from .views import Cart_user, cart_add, cart_del

urlpatterns = [
    path('', Cart_user.as_view(), name='cart_user'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('delete/<int:cart_id>/', cart_del, name='cart_del'),
]
