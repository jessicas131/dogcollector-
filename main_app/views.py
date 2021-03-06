from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Dog, Toy
from .forms import FeedingForm
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
  # this is for the toys that the dog doesnt have 
  toys_dog_doesnt_have = Toy.objects.exclude(id__in = dog.toys.all().values_list('id'))
  #grab the feeding forms you made in forms.py 
  feeding_form = FeedingForm()
  return render(request, 'dogs/detail.html', {
    # include the dog and feeding_form in the context
    'dog': dog, 'feeding_form': feeding_form,
    # display the toys the dog doesnt have with this:
    'toys': toys_dog_doesnt_have
  })

def add_feeding(request, dog_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the dog_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    new_feeding.save()
  return redirect('detail', dog_id=dog_id)

def assoc_toy(request, dog_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Dog.objects.get(id=dog_id).toys.add(toy_id)
  return redirect('detail', dog_id=dog_id)


class DogCreate(CreateView):
  model = Dog
  fields = ['name','breed', 'description', 'age']

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