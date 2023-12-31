from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_artwork, name="all_artwork"),
    path('<int:artwork_id>/', views.artwork_detail, name="artwork_detail"),
]
