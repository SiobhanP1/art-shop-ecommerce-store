from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from .forms import OrderForm
from products.models import Artwork
from .models import OrderItem, Order
from basket.contexts import basket_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """Add save_info to payment intent"""
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Your payment could not be processed.")
        return HttpResponse(content=e, status=400)


def checkout(request):
    """A view to return the checkout page"""

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            order_form.save() # Remove?
            for item_id, quantity in basket.items():
                try:
                    artwork = Artwork.objects.get(id=item_id)
                    order_item = OrderItem(
                        order=order,
                        artwork=artwork,
                        )
                    order_item.save()
                except Artwork.DoesNotExist:
                    messages.error(request, ('Item not in our database.'))
                    order.delete()
                    return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'Error in form')
    else:
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


def checkout_success(request, order_number):
    """A view to display a successful checkout message and to delete the expired session"""
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f'Your order has been placed successfully. Your order number is {order_number}. A confirmation email will be sent to this email address: {order.email}')
    
    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)