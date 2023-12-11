from django.shortcuts import render


def view_basket(request):
    """A view to display the contents of the basket and totals"""
    return render(request, 'basket/basket.html')