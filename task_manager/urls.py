from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from task_manager.views import home, trigger_error

urlpatterns = [
    path('', home, name='home'),
    path('login/', RedirectView.as_view(url='/users/login/', permanent=False), name='login_redirect'),
    path('logout/', RedirectView.as_view(url='/users/logout/', permanent=False), name='logout_redirect'),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('admin/', admin.site.urls),
    path('test-error/', trigger_error, name='test_error'),
]
