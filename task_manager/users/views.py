from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import update_session_auth_hash
from task_manager.users.forms import CustomUserCreationForm

PERMISSION_DENIED_MESSAGE = "У вас нет прав для изменения"

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

class UserListView(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Вы залогинены')
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Вы разлогинены')
        return super().dispatch(request, *args, **kwargs)

class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('users')
    
    def test_func(self):
        return self.request.user.pk == self.get_object().pk
    
    def handle_no_permission(self):
        messages.error(self.request, PERMISSION_DENIED_MESSAGE)
        return redirect('users')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        password = self.request.POST.get('password')
        password_confirm = self.request.POST.get('password_confirm')
        
        if password or password_confirm:
            if password != password_confirm:
                messages.error(self.request, 'Пароли не совпадают')
                return self.form_invalid(form)
            if password and len(password) < 3:
                messages.error(self.request, 'Пароль должен содержать минимум 3 символа')
                return self.form_invalid(form)
            user.set_password(password)
            update_session_auth_hash(self.request, user)
        
        user.save()
        messages.success(self.request, 'Пользователь успешно изменен')
        return super().form_valid(form)

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('users')
    
    def test_func(self):
        return self.request.user.pk == self.get_object().pk
    
    def handle_no_permission(self):
        messages.error(self.request, PERMISSION_DENIED_MESSAGE)
        return redirect('users')
    
    def get(self, request, *args, **kwargs):
        user = self.get_object()
        if user.author_tasks.exists() or user.executor_tasks.exists():
            messages.error(request, 'Невозможно удалить пользователя, так как он связан с задачами')
            return redirect('users')
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(request, 'Пользователь успешно удален')
            return response
        except IntegrityError:
            messages.error(request, 'Невозможно удалить пользователя, так как он связан с задачами')
            return redirect('users')
