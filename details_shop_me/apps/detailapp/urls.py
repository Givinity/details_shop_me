from django.urls import path, include

from details_shop_me.apps.detailapp.views import *
from rest_framework import routers

class MyCustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(url=r'^{prefix}$',
                      mapping={'get': 'list'},
                      name='{basename}-list',
                      detail=False,
                      initkwargs={'suffix': 'List'}),
        routers.Route(url=r'^{prefix}/{lookup}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix': 'Detail'})
    ]

router = MyCustomRouter()
router.register(r'detail', DetailsViewSet, basename='detail')

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
    path('api/v1/', include(router.urls)),
    # path('api/v1/listdetails/', DetailsViewSet.as_view({'get': 'list'})),
    # path('api/v1/listdetails/<int:pk>', DetailsViewSet.as_view({'put': 'update'})),
    # path('api/v1/viewdetails/<int:pk>', DetailsViewSet.as_view({'get': 'retrieve'})),
]
