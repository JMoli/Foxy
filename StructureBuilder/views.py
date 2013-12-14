from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def path(request):

    return render(request, 'path.html', {})

def custom(request):
    return render(request, 'custom.html', {})
