from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    query = request.GET.get('q') #gets the query from my search bar
    if query:
        tasks = Task.objects.filter(title__icontains=query) #filters the task here based on title
    else:
        tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST) #creates a form
        if form.is_valid():
            form.save()
            return redirect('task_list') #redirects to the task list
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk): #updates the task
    task = get_object_or_404(Task, pk=pk) #gets the task
    if request.method == 'POST': #if the request is post
        form = TaskForm(request.POST, instance=task) #creates a form
        if form.is_valid(): #if the form is valid
            form.save()     #save the form
            return redirect('task_list')    #redirect to the task list
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk): #deletes the task
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST': 
        task.delete() #deletes the task
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_del.html', {'task': task}) 