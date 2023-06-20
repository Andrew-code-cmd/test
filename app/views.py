from django.shortcuts import render, get_object_or_404
from .models import Task

from django.views.generic import DetailView, ListView

def home(request):
    return render(request, 'index.html')

def home(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render(request, 'index.html', context)

class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    content_object_name = 'tasks'
    ordering = ['-date_posted']

class TaskDetailView(DetailView):
    model = Task






