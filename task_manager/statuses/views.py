from django.views.generic.list import ListView
from .models import Statuses


class StatusesListView(ListView):
    model = Statuses
    template_name = "statuses/statuses_list.html"
    context_object_name = "statuses"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
