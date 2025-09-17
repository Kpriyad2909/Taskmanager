from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from tasks.forms import TasksInputForm,Filters
from django.contrib.auth.decorators import  login_required

# In your views.py, update the list_tasks function

def list_tasks(request):
    tasks = Tasks.objects.all()
    
    # Instantiate the form with the GET data
    form = Filters(request.GET)
    
    # Check if the form data is valid before filtering
    if form.is_valid():
        search_query = form.cleaned_data.get('search')
        status_filter = form.cleaned_data.get('status')
        priority_filter = form.cleaned_data.get('priority')
        
        if search_query:
            tasks = tasks.filter(title__icontains=search_query)
        if status_filter:
            tasks = tasks.filter(status=status_filter)
        if priority_filter:
            tasks = tasks.filter(priority=priority_filter)

    context = {
        'result': tasks,
        'filter_form': form, # Pass the form object to the template
    }
    return render(request, "tasks/tasks_list.html", context)

@login_required
def add_tasks(request):
    if request.method == 'POST':
        form = TasksInputForm(request.POST)
        print("Priority choices:", form.fields['priority'].choices)
        print("Status choices:", form.fields['status'].choices)
        if form.is_valid():
            form.save()
            return redirect('tasks:listtasks')
    else:
        form = TasksInputForm()
        print("Priority choices:", form.fields['priority'].choices)
        print("Status choices:", form.fields['status'].choices)
    return render(request, "tasks/add_tasks.html", {'form': form})

@login_required
def edit_form(request, task_id=None):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == 'POST':
        form = TasksInputForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:listtasks')
    else:
        form = TasksInputForm(instance=task)
    return render(request, 'tasks/add_tasks.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id)
    task.delete()
    return redirect('tasks:listtasks')




    