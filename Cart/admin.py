from django.contrib import admin
from .models import CartItem,UserCart
# Register your models here.

admin.site.register(CartItem)
admin.site.register(UserCart)
