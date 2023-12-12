from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from django.contrib import messages

from .models import Artwork, Artist


def all_artwork(request):
    """A view to show all artwork including sort and search results"""

    all_artwork = Artwork.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Please enter a search query.')
                return redirect(reverse('all_artwork'))
            queries = Q(title__icontains=query) | Q(description__icontains=query) | Q(main_media__icontains=query) 
            all_artwork = all_artwork.filter(queries)

    # all_artwork refers to query, sort or view all request results
    context = {
        'all_artwork': all_artwork,
        'search_term': query,
        }
    return render(request, 'products/all_artwork.html', context)


def artwork_detail(request, artwork_id):
    """A view to show the details of any artwork"""

    artwork = get_object_or_404(Artwork, pk=artwork_id)
    context = {'artwork': artwork,}
    return render(request, 'products/artwork_detail.html', context)