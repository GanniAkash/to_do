from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task
import time

@login_required
def complete_task(request, id):
    if request.user == Task.objects.get(id=id).task_user:
        com_task = Task.objects.get(id=id)
        com_task.is_completed = not com_task.is_completed
        com_task.save()
        return HttpResponseRedirect(reverse('todo:todo-home'))
    else:
        return redirect('login')

@login_required
def delete_task(request, id):
    if request.user == Task.objects.get(id=id).task_user:
        del_task = Task.objects.get(id=id)
        del_task.delete()
        return HttpResponseRedirect(reverse('todo:todo-home'))
    else:
        return redirect('login')
    
@login_required
def add_task(request):
    if request.method == 'POST':
        if 'task' in request.POST and request.POST['task'] != '':
            if request.POST['due_date'] == '':
                new_task = Task(task=request.POST['task'], task_user=request.user)
            else:
                new_task = Task(task=request.POST['task'], due_date=request.POST['due_date'], task_user=request.user)
            new_task.save()
    return HttpResponseRedirect(reverse('todo:todo-home'))

@login_required
def home(request):
    tasks = Task.objects.filter(task_user=request.user).order_by('due_date', 'date_created')
    context = {'tasks':tasks}
    if request.method == 'POST' and 'searchSubmit' in request.POST:
        tasks = [task for task in tasks if request.POST['taskSearch'] in task.task]
        context = {'tasks':tasks}
    return render(request, 'todo/home.html', context=context)
