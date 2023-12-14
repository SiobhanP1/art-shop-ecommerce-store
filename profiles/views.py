from django.shortcuts import render

from .forms import UserProfileForm


def profile(request):
    """View to display user profile"""

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profile/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }
    return render(request, template, context)