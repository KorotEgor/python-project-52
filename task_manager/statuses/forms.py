from .models import Statuses
from django import forms


class StatuseCreateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150, required=True,
    )
    class Meta:
        model = Statuses
        fields = ["name"]
