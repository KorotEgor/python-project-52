from django.urls import path
from .views import TasksListView

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks_list'),
]