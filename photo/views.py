from django.views import generic

from .models import Photo, Album


# Create your views here.
class AlbumLV(generic.ListView):
    model = Album


class AlbumDV(generic.DetailView):
    model = Album


class PhotoDV(generic.DetailView):
    model = Photo
