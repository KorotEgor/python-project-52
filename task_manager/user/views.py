from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _

from .forms import UserCreateForm
from .models import User


class UserListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CreateUserView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'users/create.html'
    # success_url = reverse_lazy('login')
    success_url = '/'
    success_message = _('User successfully registered')


