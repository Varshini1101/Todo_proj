from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('index')
    return render(request, 'todo/index.html', {'tasks': tasks})
