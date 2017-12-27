from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=265)
    description = models.CharField(max_length=265)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=265)
    description = models.CharField(max_length=265)

    def __str__(self):
        return self.name


class Hat(models.Model):
    name = models.CharField(max_length=265)
    description = models.CharField(max_length=265)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='hat_pics')
    supplier = models.ForeignKey(Supplier, blank=True, null=True, on_delete=models.SET_NULL, related_name='suppliers')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL, related_name='categories')

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    quantity = models.PositiveIntegerField(default=0)
    GST = models.DecimalField(decimal_places=2, max_digits=8)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    client = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.client.username)

class CartItem(models.Model):
    product = models.ForeignKey(Hat, on_delete=None)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    quantity = models.PositiveIntegerField(default=0)
    cart = models.ForeignKey(ShoppingCart, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.product.name
