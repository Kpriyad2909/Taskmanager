from django.urls import path

from .views import TaskManager

urlpatterns = [
    path('tasks/', TaskManager.as_view(), name='TaskManager_list'),
]