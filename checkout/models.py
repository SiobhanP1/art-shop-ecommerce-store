from django.db import models

from products.models import Artwork
from django.db.models import Sum

import uuid


class Order(models.Model):

    order_number = models.CharField(max_length=2, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=284, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=4, decimal_places=2, null=False, default=20)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)

    def __str__(self):
        return self.order_number

    def _generate_order_number(self):
        """Generate unique order number"""
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """Override original save method to generate order number if not there"""
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def update_totals(self):
        """Update total and grand total when new order item added"""
        self.order_total = self.lineitems.aggregate(Sum(self.artwork.price))
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    artwork = models.ForeignKey(Artwork, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.artwork.title} from order {self.order.order_number}'

