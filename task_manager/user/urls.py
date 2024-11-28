from django.urls import path

from task_manager.user.views import UserListView, CreateUserView, UpdateUserView, DeleteUserView

urlpatterns = [
    path('', UserListView.as_view(), name='users_list'),
    path('create/', CreateUserView.as_view(), name='register'),
    path('<int:pk>/update/', UpdateUserView.as_view()),
    path('<int:pk>/delete/', DeleteUserView.as_view())
]