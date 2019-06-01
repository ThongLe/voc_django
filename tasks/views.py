import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import TaskForm

from .models import Task


@login_required
def list_tasks(request):
    if request.method == 'GET':
        context = {}
        return render(request, os.path.join('tasks', 'index.html'), context)

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save()
            return redirect('todos:view', task_id=task.id)

        context = {'form': form}
        return render(request, os.path.join('tasks', 'create.html'), context)


@login_required
def create_task(request):
    if request.method == 'GET':
        context = {
            'form': TaskForm()
        }
        return render(request, os.path.join('tasks', 'create.html'), context)


@login_required
def view_task(request, task_id):
    if request.method == 'GET':
        context = {
            'task': get_object_or_404(Task, pk=task_id)
        }
        return render(request, os.path.join('tasks', 'view.html'), context)

    if request.method == 'PUT':
        context = {}
        return render(request, os.path.join('tasks', 'view.html'), context)

