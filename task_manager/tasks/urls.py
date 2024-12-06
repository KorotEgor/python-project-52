from django.urls import path
from .views import TasksListView, CreateStatusView

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks_list'),
    path('create/', CreateStatusView.as_view(), name='create_task'),
]