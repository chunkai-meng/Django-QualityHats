from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.core.validators import RegexValidator
from product_app.models import Hat


class Order(models.Model):
    SHOPPINGCART = 'SC'
    SUBMITTED = 'SM'
    PAID = 'PD'
    PROCESSING = 'PS'
    SHIPPED = 'SD'
    DELIVERED = 'DD'
    STATUS_CHOICES = (
        (SHOPPINGCART, 'In Shoppingcart'),
        (SUBMITTED, 'Submitted'),
        (PAID, 'Paid'),
        (PROCESSING, 'Processing'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=SHOPPINGCART)
    submitted_date = models.DateTimeField("Submitted Date", blank=True, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, blank=True)
    GST = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    total_price = models.DecimalField(
        "Total Price", decimal_places=2, max_digits=10, blank=True, null=True)
    account = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    recipient = models.CharField("Recipient Name", max_length=256, blank=True, null=True)

    phone_regex = RegexValidator(
        regex=r'^\+?\d{8,16}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField("Phone Number", validators=[
                                    phone_regex], max_length=16, blank=True, null=True)
    street_line1 = models.CharField("Address 1", max_length=100, blank=True, null=True)
    street_line2 = models.CharField("Address 2", max_length=100, blank=True, null=True)
    zipcode = models.CharField("Zip Code", max_length=5, blank=True, null=True)
    city = models.CharField("City", default="Auckland", max_length=100, blank=True, null=True)
    state = models.CharField("State", default="New Zealand", max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    # Tell Django where to go to after submitted
    def get_absolute_url(self):
        return reverse("order_app:detail", kwargs={'pk': self.pk})


class OrderItem(models.Model):
    product = models.ForeignKey(Hat, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    quantity = models.PositiveIntegerField(default=0)
    order = models.ForeignKey(Order, blank=True, null=True,
                              on_delete=models.SET_NULL, related_name='items')

    def __str__(self):
        return self.product.name

    def subtotal(self):
        return self.price * self.quantity
