from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from mysite.views import OwnerOnlyMixin

from .models import Bookmark

# Create your views here.


class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDV(DetailView):
    model = Bookmark


class BookmarkCreateView(LoginRequiredMixin, CreateView):
    pass


class BookmarkChangeLV(LoginRequiredMixin, ListView):
    pass


class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    pass


class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    pass
