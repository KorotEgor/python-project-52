from .models import Tasks
from django import forms


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [
            "name",
            "description",
            "status",
            "executor",
        ]
