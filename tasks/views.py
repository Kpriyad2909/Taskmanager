from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from .forms import TasksInputForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

def list_tasks(request):
    searchtasks = request.GET.get('search', '')
    filterstatus = request.GET.get('status')
    filterpriority = request.GET.get('priority')
    result = Tasks.objects.all()
    if searchtasks:
        result = result.filter(title__icontains=searchtasks)
    if filterstatus:
        result = result.filter(status=filterstatus)
    if filterpriority:
        result = result.filter(priority=filterpriority)
    return render(request, "tasks/tasks_list.html", 
                 {'result': result,
                  'searchtasks':searchtasks,
                  'filterstatus': filterstatus,
                  'filterpriority': filterpriority})


def add_tasks(request):
    if request.method == 'POST':
        form = TasksInputForm(request.POST)
        print("Priority choices:", form.fields['priority'].choices)
        print("Task_status choices:", form.fields['Task_status'].choices)
        if form.is_valid():
            form.save()
            return redirect('tasks:listtasks')
    else:
        form = TasksInputForm()
        print("Priority choices:", form.fields['priority'].choices)
        print("Task_status choices:", form.fields['Task_status'].choices)
    return render(request, "tasks/add_tasks.html", {'form': form})


    
def task_form(request, task_id=None):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == 'POST':
        form = TasksInputForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:listtasks')
    else:
        form = TasksInputForm(instance=task)
    return render(request, 'tasks/add_tasks.html', {'form': form})


def delete_task(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id)
    task.delete()
    return redirect('tasks:listtasks')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('tasks:login') 
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('tasks:login')
        else:
            login(request, user)
            print("Messages at login:", list(messages.get_messages(request)))
            return redirect('tasks:listtasks') 

    return render(request, 'tasks/login.html')
     

def signup_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists!")
            return redirect('tasks:signup')
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name)
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully!")
        return redirect('tasks:login')  
    return render(request, 'tasks/signup.html')

def logout_page(request):
    logout(request)
    messages.info(request, "You are logged out. Please log in to continue")
    return redirect('tasks:login')
    
