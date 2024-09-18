from pyexpat import model
from django.views.generic.detail import DetailView

from django.shortcuts import render, redirect
from .models import Creatures
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request):
    beasts = Creatures.objects.all()
    return render(request, 'teach/index.html', {'cindex': beasts})