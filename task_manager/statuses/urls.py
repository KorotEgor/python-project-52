from django.urls import path

from task_manager.statuses.views import StatusesListView

urlpatterns = [
    path('', StatusesListView.as_view(), name='statuses_list'),
]
