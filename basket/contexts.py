from django.shortcuts import get_object_or_404
from django.conf import settings

from products.models import Artwork

def basket_contents(request):
    """"""
    basket_items = []
    total = 0
    number_items = 0
    basket = request.session.get('basket', {})

    for item_id in basket.items():
        artwork = get_object_or_404(Artwork, pk=item_id)
        total += artwork.price
        number_items += 1
        basket_items.append({
            'item_id': item_id,
            'artwork': artwork,
        })

    grand_total = total + settings.STANDARD_DELIVERY_COST

    context = {
        'basket_items': basket_items,
        'total': total, 
        'number_items': number_items,
        'standard_delivery_cost': settings.STANDARD_DELIVERY_COST,
        'grand_total': grand_total,
    }

    return context

