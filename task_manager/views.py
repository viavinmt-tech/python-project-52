from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django_filters.views import FilterView
from django.http import HttpResponse
from .models import Status, Task, Label
from .forms import StatusForm, TaskForm, LabelForm
from .filters import TaskFilter

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.first_name = request.POST.get('first_name', '')
            user.last_name = request.POST.get('last_name', '')
            user.save()
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses.html'
    context_object_name = 'statuses'

class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'status_create.html'
    success_url = reverse_lazy('statuses')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Статус успешно создан')
        return response

class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'status_update.html'
    success_url = reverse_lazy('statuses')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Статус успешно изменен')
        return response

class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'status_delete.html'
    success_url = reverse_lazy('statuses')
    
    def post(self, request, *args, **kwargs):
        status = self.get_object()
        if status.task_set.exists():
            messages.error(request, 'Невозможно удалить статус, потому что он используется')
            return redirect('statuses')
        messages.success(request, 'Статус успешно удален')
        return super().post(request, *args, **kwargs)

class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter
    
    def get_queryset(self):
        queryset = Task.objects.all()
        only_self = self.request.GET.get('only_self')
        if only_self == 'on':
            queryset = queryset.filter(author=self.request.user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_only_self'] = self.request.GET.get('only_self') == 'on'
        return context

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_create.html'
    success_url = reverse_lazy('tasks')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['executor'].queryset = User.objects.all()
        form.fields['labels'].queryset = Label.objects.all()
        return form
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Задача успешно создана')
        return response

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_update.html'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Задача успешно изменена')
        return response

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('tasks')
    
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        if task.author != request.user:
            messages.error(request, 'Задачу может удалить только ее автор')
            return redirect('tasks')
        messages.success(request, 'Задача успешно удалена')
        return super().post(request, *args, **kwargs)

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels.html'
    context_object_name = 'labels'

class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'label_create.html'
    success_url = reverse_lazy('labels')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Метка успешно создана')
        return response

class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'label_update.html'
    success_url = reverse_lazy('labels')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Метка успешно изменена')
        return response

class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'label_delete.html'
    success_url = reverse_lazy('labels')
    
    def post(self, request, *args, **kwargs):
        label = self.get_object()
        if label.task_set.exists():
            messages.error(request, 'Невозможно удалить метку, потому что она используется')
            return redirect('labels')
        messages.success(request, 'Метка успешно удалена')
        return super().post(request, *args, **kwargs)

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
        user = form.save(commit=False)
        password = self.request.POST.get('password')
        password_confirm = self.request.POST.get('password_confirm')
        if password and password == password_confirm:
            user.set_password(password)
        user.save()
        messages.success(self.request, 'Пользователь успешно изменен')
        return super().form_valid(form)

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('users')
    
    def test_func(self):
        return self.request.user.pk == self.get_object().pk
    
    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для изменения')
        return redirect('users')
    
    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if user.author_tasks.exists() or user.executor_tasks.exists():
            messages.error(request, 'Невозможно удалить пользователя, так как он связан с задачами')
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        messages.success(request, 'Пользователь успешно удален')
        return super().post(request, *args, **kwargs)

def trigger_error(request):
    a = None
    a.hello()
    return HttpResponse("This will not be reached")
