from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserProfileForm
from .models import UserProfile


@login_required
def profile(request):
    """View to display user profile"""

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated.')
        else:
            messages.error(request, 'Could not update profile.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profile/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }
    return render(request, template, context)