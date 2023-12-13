from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """Update order totals when a new item is added to the order"""
    instance.order.update_totals()