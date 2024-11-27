from django.urls import path

from task_manager.user.views import UserListView, CreateUserView

urlpatterns = [
    path('', UserListView.as_view(), name='users_list'),
    path('create/', CreateUserView.as_view(), name='registration'),
]