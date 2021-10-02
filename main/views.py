from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    return render(request, template_name='main/index.html')

def form(request):
    return render(request, template_name='main/form.html')
