from django.db import models
from django.contrib.auth.models import User
from details_shop_me.apps.detailapp.models import Details

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Details, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'