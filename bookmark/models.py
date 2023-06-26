from django.db import models

# Create your models here.


class Bookmark(models.Model):
    title = models.CharField("TITLE", max_length=100, blank=True)  # 'TITLE' 데이터베이스 이름
    url = models.URLField("URL", unique=True)

    def __str__(self) -> str:
        return self.title
