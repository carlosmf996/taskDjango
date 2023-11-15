from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Task
from .forms import TaskForm
from django.http import HttpResponseRedirect

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
        tasks = Task.objects.all()
        return render(request, 'tasks/task_list.html', {'tasks': tasks})
            


class TaskDetails(View):

    def get(self, request, pk):
        tasks = get_object_or_404(Task, pk=pk)  
        return render(request, 'tasks/task_details.html', {'tasks': tasks})
    

class New(View):

    def get(self, request):
        form=TaskForm()
        return render(request, 'tasks/new.html', {'form': form})
    
    def post(self, request):
        form=TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]
            completado = form.cleaned_data["completado"]

            Task.objects.create(title = title, text = text, completado = completado)
            #form.save()
            return redirect('task_list')
        return render(request, 'tasks/new.html', {'form': form})