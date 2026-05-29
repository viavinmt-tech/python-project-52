from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Task Manager</h1>")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
]
