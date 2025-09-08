from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from .forms import TasksInputForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

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
        if form.is_valid():
            task = form.save(commit=False)
            task.status = 'Pending'  # set default status
            task.save()
            return redirect('tasks:listtasks')
    else:
        form = TasksInputForm()
    return render(request, "tasks/add_tasks.html", {'form': form})

def mark_task_as_completed(request, task_id):
    if request.method == "POST":
        status_value = request.POST.get("status")
        task = get_object_or_404(Tasks, id=task_id)
        if status_value == "true":
            task.status = "Completed"
        else:
            task.status = "Pending"
        task.save()
    return redirect('tasks:listtasks')

def delete_task(request):
    if request.method == "POST":
        task_ids = request.POST.getlist('delete_task')
        if task_ids:
            Tasks.objects.filter(id__in=task_ids).delete()
    return redirect('tasks:listtasks')

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

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('tasks:login')  # Use name from urls.py

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('tasks:login')
        else:
            login(request, user)
            return redirect('tasks:listtasks')  # Redirect to task list after login

    return render(request, 'tasks/login.html')
     

# SIGNUP VIEW
def signup_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists!")
            return redirect('tasks:signup')
        # Create new user
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully! Please log in to continue")
        return redirect('tasks:login')  # Redirect to login after signup
    return render(request, 'tasks/signup.html')