from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task

@login_required
def delete_task(request, id):
    if request.user == Task.objects.get(id=id).task_user:
        del_task = Task.objects.get(id=id)
        del_task.delete()
        return HttpResponseRedirect(reverse('todo:todo-home'))
    else:
        return redirect('login')

@login_required
def home(request):
    tasks = Task.objects.filter(task_user=request.user).order_by('due_date', 'date_created')
    context = {'tasks':tasks}
    if request.POST and request.POST['task'] != '':
        if request.POST['due_date'] == '':
            new_task = Task(task=request.POST['task'], task_user=request.user)
        else:
            new_task = Task(task=request.POST['task'], due_date=request.POST['due_date'], task_user=request.user)
        new_task.save()
        print(new_task.id)
    return render(request, 'todo/home.html', context=context)
