from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task
from datetime import datetime
import pytz

def delete_task(request, id):
    del_task = Task.objects.get(id=id)
    del_task.delete()
    return HttpResponseRedirect(reverse('todo:todo-home'))

def home(request):
    tasks = Task.objects.order_by('date_created').reverse()
    context = {'tasks':tasks}
    if request.POST and request.POST['task'] != '':
        if request.POST['due_date'] == '':
            ct = nai
            print('hi', request.POST['due_date'])
            new_task = Task(task=request.POST['task'])
        else:
            new_task = Task(task=request.POST['task'], due_date=request.POST['due_date'])
        new_task.save()
    return render(request, 'todo/base.html', context=context)
