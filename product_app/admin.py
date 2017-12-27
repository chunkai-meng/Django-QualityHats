from django.contrib import admin
from .models import Supplier, Category, Hat, ShoppingCart, CartItem

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Hat)
admin.site.register(ShoppingCart)
admin.site.register(CartItem)
