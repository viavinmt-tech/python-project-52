from django.db import models
from django.contrib.auth.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label

class Task(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Имя')
    description = models.TextField(blank=True, verbose_name='Описание')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус')
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='author_tasks', verbose_name='Автор'
    )
    executor = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='executor_tasks', 
        blank=True, null=True, verbose_name='Исполнитель'
    )
    labels = models.ManyToManyField(Label, blank=True, verbose_name='Метки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
