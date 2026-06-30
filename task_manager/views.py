from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

@require_http_methods(["GET"])
def home(request):
    return render(request, 'home.html')

@require_http_methods(["GET"])
def trigger_error(request):
    a = None
    a.hello()
    return HttpResponse("This will not be reached")
