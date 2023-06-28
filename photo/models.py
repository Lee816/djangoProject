from django.db import models
from django.urls import reverse

from .fields import ThumbnailImageField

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField("One Line Description", max_length=100, blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self): # 정의된 객체를 지칭하는 url을 반환
        return reverse("photo:album_detail", args=(self.id,))


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField("TITLE", max_length=30)
    description = models.TextField("Photo Description", blank=True)
    image = ThumbnailImageField(upload_to="photo/%Y/%m")  # 사진에 대한 원본이미지와 썸네일 이미지를 모두 젖아할 수 있는 필드로 커스텀 필드
    upload_dt = models.DateTimeField("Uploaded Date", auto_now_add=True)

    class Meat:
        ordering = ("title",)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("photo:photo_detail", kwargs=(self.id,))
