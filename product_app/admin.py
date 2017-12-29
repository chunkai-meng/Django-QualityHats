from django.contrib import admin
from .models import Supplier, Category, Hat

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Hat)
