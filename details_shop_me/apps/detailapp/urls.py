from django.urls import path

from details_shop_me.apps.detailapp.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('catalog/', Catalog.as_view(), name='catalog'),
    path('info/', info, name='info'),
    path('contacts/', contacts, name='contacts'),
    path('cart/', Cart.as_view(), name='cart'),
    path('category/<slug:cat_slug>/', DetailsCategory.as_view(), name='category'),
]
