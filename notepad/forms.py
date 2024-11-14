from django import forms

from notepad.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            "type": "datetime-local",
        }),
    )

    class Meta:
        model = Task
        fields = "__all__"


class TagForm(forms.ModelForm):
    tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Tag
        fields = "__all__"
