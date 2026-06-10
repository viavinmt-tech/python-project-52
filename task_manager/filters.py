import django_filters
from django import forms
from .models import Task, Status, Label
from django.contrib.auth.models import User

class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Статус'
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Исполнитель'
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        field_name='labels',
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Метка'
    )
    
    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
