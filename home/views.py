from django.shortcuts import render


def index(request):
    """A view to return the home page"""
    return render(request, 'home/index.html')


def about(request):
    """A view to return the about page"""
    return render(request, 'home/about.html')


def delivery(request):
    """A view to return the delivery page"""
    return render(request, 'home/delivery.html')