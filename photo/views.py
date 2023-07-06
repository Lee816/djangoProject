from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from mysite.views import OwnerOnlyMixin
from photo.forms import PhotoInlineFormSet

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


class AlbumPhotoCV(LoginRequiredMixin, generic.CreateView):
    model = Album
    fields = ("name", "description")
    success_url = reverse_lazy("photo:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["formset"] = PhotoInlineFormSet(
                self.request.POST, self.request.FILES
            )
        else:
            context["formset"] = PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context["formset"]
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class AlbumPhotoUV(OwnerOnlyMixin, generic.UpdateView):
    model = Album
    fields = ("name", "description")
    success_url = reverse_lazy("photo:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["formset"] = PhotoInlineFormSet(
                self.request.POST, self.request.FILES, instance=self.object
            )
        else:
            context["formset"] = PhotoInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["formset"]
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
