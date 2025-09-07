from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tasks
from .forms import TasksInputForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def list_tasks(request):
    searchtasks = request.GET.get('search', '')
    filterstatus = request.GET.get('status')
    filterpriority = request.GET.get('priority')
    result = Tasks.objects.all()
    if searchtasks:
        result = result.filter(title__icontains=searchtasks)
        print("Search:", searchtasks)
    if filterstatus:
        result = result.filter(status=filterstatus)
        print("Status:", filterstatus)
    if filterpriority:
        result = result.filter(priority=filterpriority)
        print("Priority:", filterpriority)
        print("Result count:", result.count())
        #result = result.filter(priority=filterpriority.capitalize())
    return render(request, "tasks/tasks_list.html", 
                 {'result': result,
                  'searchtasks':searchtasks,
                  'filterstatus': filterstatus,
                  'filterpriority': filterpriority})


def add_tasks(request):
     if request.method == 'POST':
        form = TasksInputForm(request.POST)
        if form.is_valid():
         #form.save()
         Tasks.objects.create(
             title=form.cleaned_data['title'],
             description=form.cleaned_data['description'],
             duedate=form.cleaned_data['duedate'],
             priority=form.cleaned_data['priority'],
             # Default status is Pending
             status='Pending', 
         )
         return redirect('tasks:listtasks')
        else:
            print("Form errors:", form.errors)
     else:
        form = TasksInputForm()
     return render(request,"tasks/add_tasks.html", 
                  {'form': form}) 


def mark_task_as_completed(request, task_id):
    if request.method == "POST":
        status_value = request.POST.get("status")
        task = get_object_or_404(Tasks, id=task_id)
        if status_value == "true":
            task.status = "Completed"
        else:
            task.status = "Pending"
        task.save()
    return redirect('tasks:listtasks')  # or wherever you want to redirect


def delete_task(request):
    #print("POST data:", request.POST)
    if request.method == "POST":
        task_id = request.POST.getlist('delete_task')
        if task_id:
          Tasks.objects.filter(id__in=task_id).delete()
    return redirect('tasks:listtasks') 


def task_form(request, task_id=None):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == 'POST':
        form = TasksInputForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.duedate = form.cleaned_data['duedate']
            task.priority = form.cleaned_data['priority']
            task.save()
            return redirect('tasks:listtasks')
    else:
        form = TasksInputForm(initial={
            'title': task.title,
            'description' : task.description,
            'duedate': task.duedate,
            'priority': task.priority,
        })
    return render(request, 'tasks/add_tasks.html', {'form': form})

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
            return redirect('tasks:listtasks')  
    return render(request, 'tasks/login.html')
     

def signup_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists")
            return redirect('tasks:signup')
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully! Please log in to continue")
        return redirect('tasks:login')  
    return render(request, 'tasks/signup.html')








 

