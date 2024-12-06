from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from task_manager.mixins import CheckLoggedInMixin
from .models import Tasks
from .forms import TaskCreateForm

class TasksListView(CheckLoggedInMixin, ListView):
    template_name = 'tasks/tasks_list.html'
    model = Tasks
    context_object_name = 'tasks'


class CreateStatusView(CheckLoggedInMixin, SuccessMessageMixin, CreateView):
    model = Tasks
    form_class = TaskCreateForm
    template_name = "tasks/CU_form.html"
    extra_context = {
        "title": _("Create task"),
        "btn_name": _("Create task"),
    }
    success_url = reverse_lazy("tasks_list")
    success_message = _("Task successfully created")
