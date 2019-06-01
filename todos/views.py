import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def todos(request):
    if request.method == 'GET':
        context = {}
        return render(request, os.path.join('todos', 'index.html'), context)

    if request.method == 'POST':
        context = {}
        return render(request, os.path.join('todos', 'index.html'), context)


@login_required
def todo(request):
    if request.method == 'GET':
        context = {}
        return render(request, os.path.join('todos', 'view.html'), context)

    if request.method == 'PUT':
        context = {}
        return render(request, os.path.join('todos', 'view.html'), context)
