from django.db import models

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
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
