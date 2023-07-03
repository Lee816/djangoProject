from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Bookmark(models.Model):
    # '이름' -> admin 사이트에서 나타나는 별칭(verbose_name)
    title = models.CharField("TITLE", max_length=100, blank=True)
    url = models.URLField("URL", unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
