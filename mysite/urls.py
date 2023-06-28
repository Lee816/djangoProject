"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import (
    static,
)  # static()함수는 정적 파일을 처리하기 위해 그에 맞는 URL패턴을 반환한느 함수
from django.conf import (
    settings,
)  # settings 변수는 settings.py 모듈에서 정의한 항목들을 담고 있는 개체를 가리키는 reference

from .views import HomeView
from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("bookmark/", BookmarkLV.as_view(), name="index"),
    path("bookmark/<int:pk>/", BookmarkDV.as_view(), name="detail"),
    path("photo/", include("photo.urls")),  # phto 앱의 url 처리
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # 기존 URL패턴에 static() 함수가 반환하는 패턴을 추가
