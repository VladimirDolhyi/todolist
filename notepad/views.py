from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
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


class ToggleCompleteTaskView(View):
    @staticmethod
    def post(request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done  # Переключаем статус задачи
        task.save()  # Сохраняем изменения

        # Получаем текущие параметры запроса
        page = request.POST.get("page", 1)  # По умолчанию 1, если не указан

        # Используем reverse для перенаправления на маршрут 'notepad:index'
        return HttpResponseRedirect(f'{reverse("notepad:index")}?page={page}')
