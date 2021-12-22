from django.db import models

from Products.models import Product


# Модель корзины юзера
class UserCart(models.Model):
    slug = models.SlugField(unique=True)
    user_name = models.CharField(max_length=100, unique=True)

    def get_full_price(self):
        return sum([i.get_price() for i in self.user.all()])

    def __str__(self):
        return self.user_name


# Модель товара юзера в корзине
class CartItem(models.Model):
    user = models.ManyToManyField(UserCart, blank=True, related_name="user")
    products = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField()
    username = models.CharField(max_length=300)

    def get_price(self):
        return self.count * self.products.price

    def __str__(self):
        return f"{self.username}({self.products.title})"
