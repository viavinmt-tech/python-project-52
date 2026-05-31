from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    return render(request, 'home.html')

class UserListView(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Пользователь успешно зарегистрирован')
        return response

class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = 'user_update.html'
    success_url = reverse_lazy('users')
    
    def test_func(self):
        return self.request.user.pk == self.get_object().pk
    
    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для изменения')
        return redirect('users')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Пользователь успешно изменен')
        return response

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('users')
    
    def test_func(self):
        return self.request.user.pk == self.get_object().pk
    
    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для изменения')
        return redirect('users')
    
    def post(self, request, *args, **kwargs):
        messages.success(request, 'Пользователь успешно удален')
        return super().post(request, *args, **kwargs)

class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Вы залогинены')
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Вы разлогинены')
        return super().dispatch(request, *args, **kwargs)

urlpatterns = [
    path('', home, name='home'),
    path('users/', UserListView.as_view(), name='users'),
    path('users/create/', UserCreateView.as_view(), name='register'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
