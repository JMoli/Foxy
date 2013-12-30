from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def style(request, style):
    return render(request, 'style.html', {})
  
def material(request):
    return render(request, 'custom.html', {'length': request.session['length']})

def builder(request):
    return render(request, 'custom.html', {'length': request.session['length']})
