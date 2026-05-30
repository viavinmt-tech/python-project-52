from django.contrib import admin
from django.urls import path
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def users(request):
    return render(request, 'users.html', {'users': []})

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

urlpatterns = [
    path('', home, name='home'),
    path('users/', users, name='users'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('admin/', admin.site.urls),
]
