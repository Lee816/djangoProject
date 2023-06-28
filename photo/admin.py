from django.contrib import admin

from .models import Album, Photo

# Register your models here.


class PhotoInline(admin.StackedInline): 
    # 외래키로 연결된 Album,Photo 테이블 간에는 일대다 관계가 성립되어 앨범 객체를 보여줄때 객체에 연결된 사진 객체들을 같이 보여줄 수 있다.
    # 같이 보여주는 형식은 StackedInline(세로로나열) 과 TabularInline(테이블모양처럼 행으로 나열) 두 가지가 있다.
    model = Photo
    extra = 1 # 객체를 새로 추가 하는 폼의 갯수


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    list_display = ("id", "name", "description")


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "upload_dt")
