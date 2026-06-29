from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Имя')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    
    class Meta:
        app_label = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['id']
    
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Имя')
    description = models.TextField(blank=True, verbose_name='Описание')
    status = models.ForeignKey('Status', on_delete=models.PROTECT, verbose_name='Статус')
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='author_tasks', verbose_name='Автор'
    )
    executor = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='executor_tasks', 
        blank=True, null=True, verbose_name='Исполнитель'
    )
    labels = models.ManyToManyField('Label', blank=True, verbose_name='Метки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    class Meta:
        app_label = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Имя')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    class Meta:
        app_label = 'labels'
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'
        ordering = ['id']
    
    def __str__(self):
        return self.name

def get_full_name(self):
    return f"{self.first_name} {self.last_name}".strip()

User.add_to_class('fullName', property(get_full_name))
