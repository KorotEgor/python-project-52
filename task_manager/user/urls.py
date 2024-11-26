from django.urls import path

from task_manager.user.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='user_index'),
]