from decimal import Decimal
from django.conf import settings
from details_shop_me.apps.detailapp.models import Details


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get()