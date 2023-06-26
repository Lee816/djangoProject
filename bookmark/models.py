from django.db import models

# Create your models here.


class Bookmark(models.Model):
    # '이름' -> admin 사이트에서 나타나는 별칭(verbose_name)
    title = models.CharField("TITLE", max_length=100, blank=True)
    url = models.URLField("URL", unique=True)

    def __str__(self) -> str:
        return self.title
