from django.urls import path
from .views import BookmarkLV, BookmarkDV

app_name = "bookmark"
urlpatterns = [
    path("bookmark/", BookmarkLV.as_view(), name="index"),
    path("bookmark/<int:pk>/", BookmarkDV.as_view(), name="detail"),
]
