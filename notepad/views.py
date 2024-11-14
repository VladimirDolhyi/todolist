from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from notepad.forms import TaskForm, TagForm
from notepad.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "notepad/index.html"
    paginate_by = 3


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("notepad:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("notepad:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("notepad:index")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("notepad:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("notepad:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("notepad:tag-list")


class ToggleConfirmTaskView(View):
    @staticmethod
    def post(request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done  # Переключаем статус задачи
        task.save()  # Сохраняем изменения
        return redirect("notepad:index")  # Перенаправляем на страницу со списком задач
