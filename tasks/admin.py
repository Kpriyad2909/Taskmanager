"""from django.contrib import admin
from .models import Tasks

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority', 'status', 'user', 'duedate']
    list_filter = ['priority', 'status', 'user']
    search_fields = ['title', 'description']"""

from django.contrib import admin
from .models import Tasks


admin.site.register(Tasks)

