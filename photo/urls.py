from django.urls import path
from . import views

app_name = "photo"
urlpatterns = [
    path("", views.AlbumLV.as_view(), name="index"),
    path("album", views.AlbumLV.as_view(), name="albim_list"),
    path("album/<int:pk>/", views.AlbumDV.as_view(), name="album_detail"),
    path("photo/<int:pl>/", views.PhotoDV.as_veiw(), name="photo_detail"),
]
