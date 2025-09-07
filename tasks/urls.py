from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('login/',views.login_page, name = "login"),
    path('signup/',views.signup_page, name = "signup"),
    path("", views.list_tasks, name = "listtasks"),
    path("add/",views.add_tasks,name = "addtasks"),
    path('marktaskascompleted/<int:task_id>/', views.mark_task_as_completed, name='marktaskascompleted'),
    path("delete/", views.delete_task, name="deletetask"),
    path('edit/<int:task_id>/', views.task_form, name='edit_task'), 
]

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/add/
# http://127.0.0.1:8000//update/task_id/status/completed/
# http://127.0.0.1:8000/delete/
# http://127.0.0.1:8000/login/
# http://127.0.0.1:8000/signup/
