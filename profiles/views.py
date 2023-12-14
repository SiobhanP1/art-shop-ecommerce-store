from django.shortcuts import render


def profile(request):
    """View to display user profile"""
    template = 'profile/profile.html'
    context = {}
    return render(request, template, context)