from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from mysite.views import OwnerOnlyMixin

from .models import Photo, Album


# Create your views here.
class AlbumLV(generic.ListView):
    model = Album


class AlbumDV(generic.DetailView):
    model = Album


class PhotoDV(generic.DetailView):
    model = Photo


class PhotoCV(LoginRequiredMixin, generic.CreateView):
    model = Photo
    fields = ("album", "title", "image", "description")
    success_url = reverse_lazy("photo:index")


class PhotoChangeLV(LoginRequiredMixin, generic.ListView):
    model = Photo
    template_name = "photo/photo_change_list.html"

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)


class PhotoUV(OwnerOnlyMixin, generic.UpdateView):
    model = Photo
    success_url = reverse_lazy("photo:index")


class PHotoDelV(OwnerOnlyMixin, generic.DeleteView):
    model = Photo
    success_url = reverse_lazy("photo:index")


class AlbumChangeLV(LoginRequiredMixin, generic.ListView):
    model = Album
    template_name = "photo/album_change_list.html"

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)


class AlbumDelV(OwnerOnlyMixin, generic.DeleteView):
    model = Album
    success_url = reverse_lazy("photo:index")
