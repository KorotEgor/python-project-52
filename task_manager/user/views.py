from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _

from .forms import UserCreateForm
from .models import User
from task_manager.mixins import CheckLoggedInMixin, CheckUserPermissionMixin, DeleteProtectionMixin


class UserListView(ListView):
    model = User
    template_name = "users/users_list.html"
    context_object_name = "users"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CreateUserView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = "users/CU_form.html"
    extra_context = {
        "title": _("Register"),
        "btn_name": _("Register"),
    }
    success_url = reverse_lazy("login")
    success_message = _("User successfully registered")


class UpdateUserView(CheckLoggedInMixin, CheckUserPermissionMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = "users/CU_form.html"
    permission_message = _("You do not have permission to change another user.")
    permission_url = reverse_lazy('users_list')
    extra_context = {
        "title": _("Change user"),
        "btn_name": _("Change"),
    }
    success_url = reverse_lazy("users_list")
    success_message = _("User successfully changed")


class DeleteUserView(CheckLoggedInMixin, CheckUserPermissionMixin, DeleteProtectionMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = "users/delete_form.html"
    success_url = reverse_lazy("users_list")
    success_message = _("User successfully deleted")
    permission_message = _("You do not have permission to delete another user.")
    permission_url = reverse_lazy('users_list')
    protected_message = _('Unable to delete a user because he is being used')
    protected_url = reverse_lazy('users')
