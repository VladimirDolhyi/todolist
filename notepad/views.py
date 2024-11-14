from django.views import generic

from notepad.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "notepad/index.html"
    queryset = Task.objects.prefetch_related("tags")
    paginate_by = 4


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10
