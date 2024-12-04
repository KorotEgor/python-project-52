from .models import Statuses
from django import forms


class StatusCreateForm(forms.ModelForm):
    class Meta:
        model = Statuses
        fields = ["name"]
