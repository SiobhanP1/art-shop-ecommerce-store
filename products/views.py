from django.shortcuts import render
from .models import Artwork, Artist


def all_artwork(request):
    """A view to show all artwork including sort and search results"""

    all_artwork = Artwork.objects.all()
    context = {'all_artwork': all_artwork,}
    return render(request, 'products/all_artwork.html', context)
