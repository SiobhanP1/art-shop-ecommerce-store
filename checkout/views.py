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
        'stripe_public_key': 'pk_test_51OMu79DWBoCihvaUVsCYsnNxaTFImnaKB1n6lULQTmGLkwzkVNy4pGJ1ayCBN75sTCdr8yQcnhXBy5FmrL9sPLpn00Xc8fu5s5',
        'client_secret': 'test_secret_key',
    }
    return render(request, template, context)