from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.conf import settings
from django.db.models import Q

from .models import Post
from .forms import PostSearchForm

# Create your views here.


class PostLV(generic.ListView):
    model = Post
    template_name = "blog/post_all.html"
    context_object_name = "posts"
    paginate_by = 2


class PostDV(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["disqus_short"] = f"{settings.DISQUS_SHORTNAME}"
        context["disqus_id"] = f"post-{self.object.id}-{self.object.slug}"
        context[
            "disqus_url"
        ] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context["disqus_title"] = f"{self.object.slug}"
        return context


class PostAV(generic.ArchiveIndexView):
    model = Post
    date_field = "modify_dt"


class PostYAV(generic.YearArchiveView):
    model = Post
    date_field = "modify_dt"
    make_object_list = True


class PostMAV(generic.MonthArchiveView):
    model = Post
    date_field = "modify_dt"
    month_format = "%m"


class PostDAV(generic.DayArchiveView):
    model = Post
    date_field = "modify_dt"
    month_format = "%m"


class PostTAV(generic.TodayArchiveView):
    model = Post
    date_field = "modify_dt"
    template_name = "blog/post_archive_day.html"


class TagCloudTV(generic.TemplateView):
    template_name = "taggit/taggit_cloud.html"


class TaggedObjectLV(generic.ListView):
    template_name = "taggit/taggit_post_list.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get("tag"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tagname"] = self.kwargs["tag"]
        return context


class SearchFormView(generic.FormView):
    form_class = PostSearchForm
    template_name = "blog/post_search.html"

    def form_valid(self, form: Any) -> HttpResponse:
        searchWord = form.cleaned_data["search_word"]
        post_list = Post.objects.filter(
            Q(title__icontains=searchWord)
            or Q(description__icontains=searchWord)
            or Q(content__icontains=searchWord)
        ).distinct()

        context = {}
        context["form"] = form
        context["search_term"] = searchWord
        context["object_list"] = post_list

        return render(self.request, self.template_name, context)
