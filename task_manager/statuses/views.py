from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from .models import Statuses


class StatusesListView(ListView):
    model = Statuses
    template_name = "statuses/statuses_list.html"
    context_object_name = "statuses"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CreateStatusView(SuccessMessageMixin, CreateView):
    model = Statuses
    fields = "__all__"
    template_name = "statuses/create_status.html"
    extra_context = {
        "title": _("Statuses"),
        "btn_name": _("Create status"),
    }
    success_url = reverse_lazy("statuses_list")
    success_message = _("Status successfully created")
