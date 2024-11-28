from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib import messages

from .forms import UserCreateForm
from .models import User


class UserListView(ListView):
    model = User
    template_name = "users/users_list.html"
    context_object_name = "users"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CreateUserView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = "users/user_form.html"
    extra_context = {"title": _("Register")}
    # success_url = reverse_lazy('login')
    success_url = "/"
    success_message = _("User successfully registered")


class AccessCheckMixin:
    def get_permission(self):
        return self.request.user.pk == self.get_object().pk

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            text = _("You are not authorized! Please log in.")
            messages.error(request, messages.error(self.request, text))
            return redirect("user_form")

        elif not self.get_permission():
            text = _("You do not have permission.")
            messages.error(request, messages.error(self.request, text))
            return redirect("users_list")

        return super().dispatch(request, *args, **kwargs)


class UpdateUserView(SuccessMessageMixin, AccessCheckMixin, UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = "users/user_form.html"
    extra_context = {"title": _("Change user")}
    # success_url = reverse_lazy('users_list')
    success_url = "/users/users_list"
    success_message = _("User successfully changed")
