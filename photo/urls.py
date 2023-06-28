from django.urls import path
from . import views

app_name = "photo"
urlpatterns = [
    path("", views.AlbumLV.as_view(), name="index"),
    path("album", views.AlbumLV.as_view(), name="albim_list"),
    path("album/<int:pk>/", views.AlbumDV.as_view(), name="album_detail"),
    path("photo/<int:pl>/", views.PhotoDV.as_veiw(), name="photo_detail"),
]

# from django.views.generic import ListView, DetailView

# urlpatterns = [
#     path("", ListView.as_view(model = Album), name="index"),
#     path("album", ListView.as_view(model = Album), name="albim_list"),
#     path("album/<int:pk>/", DetailView.as_view(model = Album), name="album_detail"),
#     path("photo/<int:pl>/", DetailView.as_veiw(model = Photo), name="photo_detail"),
# ]
