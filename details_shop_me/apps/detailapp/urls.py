from django.urls import path

from details_shop_me.apps.detailapp.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('catalog/', Catalog.as_view(), name='catalog'),
    path('info/', info, name='info'),
    path('contacts/', contacts, name='contacts'),
    path('detail-info/<slug:detail_slug>/', ShowDetail.as_view(), name='detail'),
    path('category/<slug:cat_slug>/', DetailsCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('search/', Search.as_view(), name='search'),
    path('api/v1/listdetails/', ListAPIDetails.as_view()),
    path('api/v1/listdetails/<int:pk>', UpdateAPIDetails.as_view()),
    path('api/v1/viewdetails/<int:pk>', ViewAPIDetails.as_view()),
]
