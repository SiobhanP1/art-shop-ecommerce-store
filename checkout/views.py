from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """A view to return the checkout page"""
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Empty basket.")
        return redirect(reverse('all_artwork'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }
    return render(request, template, context)