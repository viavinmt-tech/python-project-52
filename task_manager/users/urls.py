from django.urls import path
from task_manager.users.views import (
    register_view,
    UserListView,
    CustomLoginView,
    CustomLogoutView,
    UserUpdateView,
    UserDeleteView
)

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('create/', register_view, name='register'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
