from django.contrib import admin
from .models import Artwork, Artist


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'description', 'price', 'main_media', 'image', 'image_url')
    ordering = ('title',)


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'about_artist')
    ordering = ('full_name',)
    

admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Artist, ArtistAdmin)
