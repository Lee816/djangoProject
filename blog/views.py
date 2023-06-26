from django.views import generic

from .models import Post

# Create your views here.


class PostLV(generic.ListView):
    model = Post
    template_name = "blog/post_all.html"
    context_object_name = "posts"
    paginate_by = 2


class PostDV(generic.DetailView):
    model = Post


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
    template_name = 'blog/post_archive_day.html'
