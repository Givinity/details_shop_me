from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from details_shop_me.apps.detailapp.models import Details

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('Cart_user', args=[str(self.id)])

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Details,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)