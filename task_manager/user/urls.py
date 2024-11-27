from django.urls import path

from task_manager.user.views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='users_list'),
    # path('create/', UserFormCreateView.as_view(), name='user_create'),
]