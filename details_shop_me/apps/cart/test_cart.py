# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth.models import User
# from django.test.client import Client
#
# from details_shop_me.apps.cart.models import Basket
# from details_shop_me.apps.detailapp.models import Details, Category
#
#
#
#
# class CartTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(
#             username='test_user', password='sitepas123')
#         self.category = Category.objects.create(name='test_cat', slug='test_cat')
#         self.product = Details.objects.create(name='Test Product', slug='test', cat=self.category)
#
#     def test_add_to_cart(self):
#         self.client.login(username='test_user', password='sitepas123')
#         response = self.client.post(reverse('cart_add', args=[self.product.id]))
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(Basket.objects.count(), 1)
#         cart_item = Basket.objects.first()
#         self.assertEqual(cart_item.product, self.product)
#         self.assertEqual(cart_item.quantity, 1)
