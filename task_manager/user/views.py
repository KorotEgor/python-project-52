from django.views.generic.list import ListView

from .models import User


class ArticleListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)