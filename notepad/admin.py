from django.contrib import admin
from django.contrib.auth.models import Group

from notepad.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "created_at", "deadline", "is_done", ]


admin.site.register(Tag)
admin.site.unregister(Group)
