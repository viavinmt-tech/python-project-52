from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django_filters.views import FilterView
from django.contrib.auth.models import User
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.filters import TaskFilter
from task_manager.labels.models import Label

class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'tasks/tasks.html'
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
    template_name = 'tasks/task_create.html'
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
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('tasks')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['executor'].queryset = User.objects.all()
        form.fields['labels'].queryset = Label.objects.all()
        return form
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Задача успешно изменена')
        return response

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks')
    
    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if task.author != request.user:
            messages.error(request, 'Задачу может удалить только ее автор')
            return redirect('tasks')
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        messages.success(request, 'Задача успешно удалена')
        return super().post(request, *args, **kwargs)

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'
