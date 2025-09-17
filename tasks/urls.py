from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path("", views.list_tasks, name = "listtasks"),
    path("add/",views.add_tasks,name = "addtasks"),
    #path('marktaskasstatus/', views.mark_task_as_status, name='marktaskasstatus'),
    path("delete/<int:task_id>/", views.delete_task, name="deletetask"),
    path('edit/<int:task_id>/', views.edit_form, name='edit_task'), 
]

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/add/
# http://127.0.0.1:8000//update/task_id/status/status/
# http://127.0.0.1:8000/delete/
# http://127.0.0.1:8000/login/
# http://127.0.0.1:8000/signup/
