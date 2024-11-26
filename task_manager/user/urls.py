from django.urls import path

from task_manager.user.views import IndexView, UserFormCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='user_index'),
    path('create/', UserFormCreateView.as_view(), name='user_create'),
]