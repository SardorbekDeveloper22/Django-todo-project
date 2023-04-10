from django.shortcuts import render
from django.views.generic import ListView,DeleteView
from django.views.generic.edit import CreateView,UpdateView
from .models import ToDo
from django.urls import reverse_lazy
# Create your views here.

class HomePageView(ListView):
    model = ToDo
    template_name = 'list.html'
    context_object_name = 'tasks'

class ToDoAddView(CreateView):
    model = ToDo
    template_name = 'add.html'
    fields = ('title', 'description','status')
class ToDoEditView(UpdateView):
    model = ToDo
    template_name = 'update.html'
    fields = ('title', 'description','status')
class ToDoDeleteView(DeleteView):
    model = ToDo
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('home')