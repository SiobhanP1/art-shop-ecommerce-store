from django.db import models


class Artwork(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False)
    artist = models.ForeignKey('Artist', null=False, blank=False, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    main_media = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.title


class Artist(models.Model):
    full_name = models.CharField(max_length=254, null=False, blank=False)
    about_artist = models.TextField()

    def __str__(self):
        return self.full_name