from django.db import models
from django.contrib.auth.models import User


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
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='hat_pics')
    supplier = models.ForeignKey(Supplier, blank=True, null=True,
                                 on_delete=models.SET_NULL, related_name='suppliers')
    category = models.ForeignKey(Category, blank=True, null=True,
                                 on_delete=models.SET_NULL, related_name='categories')

    def __str__(self):
        return self.name
