from django.db import models
from django.utils import timezone

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Имя')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['id']
    
    def __str__(self):
        return self.name
