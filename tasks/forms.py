from django import forms
from .models import Tasks

class TasksInputForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'duedate', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'duedate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'priority': forms.Select(attrs={'class': 'form-select'},choices=[('', 'All'), ('high', 'high') , ('medium', 'medium'),('low', 'low')]),
        }
