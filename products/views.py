from django.shortcuts import render, get_object_or_404
from .models import Artwork, Artist


def all_artwork(request):
    """A view to show all artwork including sort and search results"""

    all_artwork = Artwork.objects.all()
    context = {'all_artwork': all_artwork,}
    return render(request, 'products/all_artwork.html', context)


def artwork_detail(request, artwork_id):
    """A view to show the details of any artwork"""

    artwork = get_object_or_404(Artwork, pk=artwork_id)
    context = {'artwork': artwork,}
    return render(request, 'products/artwork_detail.html', context)