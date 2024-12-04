from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from .models import Statuses
from .forms import StatusCreateForm
from task_manager.mixins import CheckLoggedInMixin, DeleteProtectionMixin


class StatusesListView(ListView):
    model = Statuses
    template_name = "statuses/statuses_list.html"
    context_object_name = "statuses"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CreateStatusView(CheckLoggedInMixin, SuccessMessageMixin, CreateView):
    model = Statuses
    form_class = StatusCreateForm
    template_name = "statuses/CU_form.html"
    extra_context = {
        "title": _("Statuses"),
        "btn_name": _("Create status"),
    }
    success_url = reverse_lazy("statuses_list")
    success_message = _("Status successfully created")


class UpdateStatusView(CheckLoggedInMixin, SuccessMessageMixin, UpdateView):
    model = Statuses
    form_class = StatusCreateForm
    template_name = "statuses/CU_form.html"
    permission_message = _("You do not have permission to change another user status.")
    permission_url = reverse_lazy('statuses_list')
    extra_context = {
        "title": _("Change status"),
        "btn_name": _("Change"),
    }
    success_url = reverse_lazy("statuses_list")
    success_message = _("Status successfully changed")


class DeleteStatusView(CheckLoggedInMixin, DeleteProtectionMixin, SuccessMessageMixin, DeleteView):
    model = Statuses
    template_name = "statuses/delete_form.html"
    success_url = reverse_lazy("statuses_list")
    success_message = _("Status successfully deleted")
    permission_message = _("You do not have permission to delete another user status.")
    permission_url = reverse_lazy('statuses_list')

