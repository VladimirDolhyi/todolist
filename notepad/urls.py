from django.urls import path

from notepad.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TagCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagUpdateView,
    TagDeleteView,
    ToggleCompleteTaskView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tasks/", TaskListView.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(),
         name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(),
         name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(),
         name="task-delete"),
    path("tasks/<int:pk>/toggle-complete/", ToggleCompleteTaskView.as_view(),
         name="toggle-complete-task"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(),
         name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(),
         name="tag-delete"),
]

app_name = "notepad"
