from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path("", views.list_tasks, name = "listtasks"),
    path("add/",views.add_tasks,name = "addtasks"),
    path("update/<int:task_id>/status/<str:new_status>/", views.mark_task_as_completed, name="marktaskascompleted"),
    path("delete/", views.delete_task, name="deletetask"),
]

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/add/
# http://127.0.0.1:8000//update/task_id/status/completed/