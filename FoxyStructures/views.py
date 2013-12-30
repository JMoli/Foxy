from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html', {})
  
def path(request, structure):
    return render(request, 'path.html', {})

def church(request):
    return render(request, 'church.html', {})
