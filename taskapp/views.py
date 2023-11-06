from datetime import timezone
from django.shortcuts import render
from .models import Task

def task_list(request):

    task = Task.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'tasks/task_list.html', {'task': task})

# Create your views here.
