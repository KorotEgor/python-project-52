from django.views.generic.list import ListView

from task_manager.mixins import CheckLoggedInMixin
from .models import Tasks

class TasksListView(CheckLoggedInMixin, ListView):
    template_name = 'tasks/tasks_list.html'
    model = Tasks
    context_object_name = 'tasks'
