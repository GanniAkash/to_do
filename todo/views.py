from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task
from datetime import datetime
import pytz

@login_required
def delete_task(request, id):
    del_task = Task.objects.get(id=id)
    del_task.delete()
    return HttpResponseRedirect(reverse('todo:todo-home'))

@login_required
def home(request):
    tasks = Task.objects.order_by('due_date', 'date_created')
    context = {'tasks':tasks}
    if request.POST and request.POST['task'] != '':
        if request.POST['due_date'] == '':
            new_task = Task(task=request.POST['task'])
        else:
            new_task = Task(task=request.POST['task'], due_date=request.POST['due_date'])
        new_task.save()
    return render(request, 'todo/home.html', context=context)
