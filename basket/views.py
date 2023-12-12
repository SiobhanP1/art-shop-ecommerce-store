from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from products.models import Artwork


def view_basket(request):
    """A view to display the contents of the basket and totals"""
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """A view to add an item to the basket"""
    artwork = get_object_or_404(Artwork, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    #bag = request.session.get('bag', [])
    #if item_id in bag:
    #    messages.info(request, f"{artwork.title} is already in your basket.")
    #else: 
    #    bag.append(item_id)
    #    request.session['bag'] = bag

    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        messages.info(request, f"{artwork.title} is already in your basket.")
    else:
        basket[item_id] = 1
        request.session['basket'] = basket

    print(request.session['basket'])

    return redirect(redirect_url)
