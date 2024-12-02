from django.urls import path

from task_manager.statuses.views import StatusesListView, CreateStatusView

urlpatterns = [
    path('', StatusesListView.as_view(), name='statuses_list'),
    path('create/', CreateStatusView.as_view(), name='statuses_create'),
]
