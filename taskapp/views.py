from django.utils import timezone
from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .forms import TaskForm

# Create your views here.

"""def task_list(request):

    task = Task.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form= TaskForm()
    return render(request, 'tasks/task_list.html', {'task': task, 'form': form}) """


class TaskList(View):

        
    def get(self, request):
        form=TaskForm()
        task = Task.objects.all()
        return render(request, 'tasks/task_list.html', {'task': task, 'form': form})
    
    def post(self, request):
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('task_list')
        task = Task.objects.all()
        return render(request, 'tasks/task_list.html', {'task': task, 'form': form})