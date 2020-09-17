from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Dog, Toy

from django.http import HttpResponse


def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', { 'dogs': dogs })

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  return render(request, 'dogs/detail.html', { 'dog': dog })

class DogCreate(CreateView):
  model = Dog
  fields = '__all__'

class DogUpdate(UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model= Dog
  success_url = '/dogs/'


class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = ['name', 'color']

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']
  
class ToyDelete(DeleteView):
  model = Toy
  success_url = reverse_lazy('toys_index')