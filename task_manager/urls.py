from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .views import (
    StatusListView, StatusCreateView, StatusUpdateView, StatusDeleteView,
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView,
    LabelListView, LabelCreateView, LabelUpdateView, LabelDeleteView,
    UserDeleteView, UserUpdateView
)

def home(request):
    return render(request, 'home.html')

def users(request):
    return render(request, 'users.html', {'users': User.objects.all()})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Вы разлогинены')
        return super().dispatch(request, *args, **kwargs)

def trigger_error(request):
    a = None
    a.hello()
    return HttpResponse("This will not be reached")

urlpatterns = [
    path('', home, name='home'),
    path('users/', users, name='users'),
    path('users/create/', register_view, name='register'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('statuses/', StatusListView.as_view(), name='statuses'),
    path('statuses/create/', StatusCreateView.as_view(), name='status_create'),
    path('statuses/<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('statuses/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('labels/', LabelListView.as_view(), name='labels'),
    path('labels/create/', LabelCreateView.as_view(), name='label_create'),
    path('labels/<int:pk>/update/', LabelUpdateView.as_view(), name='label_update'),
    path('labels/<int:pk>/delete/', LabelDeleteView.as_view(), name='label_delete'),
    path('admin/', admin.site.urls),
    path('test-error/', trigger_error, name='test_error'),
]
