from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.http import HttpResponse

from products.models import Artwork


def view_basket(request):
    """A view to display the contents of the basket and totals"""
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """A view to add an item to the basket"""
    artwork = get_object_or_404(Artwork, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        messages.info(request,
                      f"{artwork.title} is already in your basket.")
    else:
        basket[item_id] = 1
        messages.success(request,
                         f"{artwork.title} successfully added to basket.")
        request.session['basket'] = basket

    print(request.session['basket'])

    return redirect(redirect_url)


def remove_from_basket(request, item_id):
    """A view to return the basket with requested changes"""
    # can remove quantity - no quantity changes in POST request object
    # quantity = int(request.POST.get('quantity'))

    artwork = get_object_or_404(Artwork, pk=item_id)
    basket = request.session.get('basket', {})

    try:
        basket.pop(item_id)
        messages.success(request,
                         f'{artwork.title} has been removed from your basket.')
        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request,
                       f'Could not remove item from basket due to {e}.')
        return HttpResponse(status=500)
