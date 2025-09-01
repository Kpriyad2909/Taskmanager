from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tasks

# Create your views here.
def list_tasks(request):
    filterstatus = request.GET.get('status')
    filterpriority = request.GET.get('priority')

    result = Tasks.objects.all()
    if filterstatus:
        result = result.filter(status=filterstatus)
    if filterpriority:
        result = result.filter(priority=filterpriority)
    
    return render(request, "tasks/tasks_list.html", {'result': result,'filterstatus': filterstatus,
        'filterpriority': filterpriority})
    
def add_tasks(request):
     if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        duedate = request.POST.get('duedate')
        priority = request.POST.get('priority')
        Tasks.objects.create(title = title,description=description ,duedate=duedate,priority=priority)
        return redirect('tasks:listtasks') 
     return render(request,"tasks/add_tasks.html")
    
def mark_task_as_completed(request, task_id, new_status):
    task = get_object_or_404(Tasks, id=task_id)
    if new_status.lower() == 'true':
        task.status = "Completed"
    else:
        task.status = "Pending"
    task.save()
    return redirect('tasks:listtasks')


def delete_task(request):
    print("POST data:", request.POST)
    if request.method == "POST":
        task_id = request.POST.getlist('delete_task')
        if task_id:
          Tasks.objects.filter(id__in=task_id).delete()
    return redirect('tasks:listtasks')




 

