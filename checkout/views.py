from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents

import stripe

def checkout(request):
    """A view to return the checkout page"""

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Empty basket.")
        return redirect(reverse('all_artwork'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
   
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount = stripe_total,
        currency = settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning('No stripe public key found.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OMu79DWBoCihvaUVsCYsnNxaTFImnaKB1n6lULQTmGLkwzkVNy4pGJ1ayCBN75sTCdr8yQcnhXBy5FmrL9sPLpn00Xc8fu5s5',
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)