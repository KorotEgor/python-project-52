from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext as _

class HomePageView(TemplateView):
    template_name = "home.html"


class UserLoginView(LoginView, SuccessMessageMixin):
    template_name = 'login.html'
    authentication_form = AuthenticationForm
    next_page = reverse_lazy('home_page')
    success_message = _("You are logged in")


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home_page')
    success_message = _("You are logged out")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
