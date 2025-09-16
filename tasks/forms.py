from django import forms
from .models import Tasks

class TasksInputForm(forms.ModelForm):
    priority = forms.ChoiceField(
        choices=[('', 'Select priority')] + list(Tasks._meta.get_field('priority').choices),
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True,
        error_messages={'required': 'Please select a priority.'}
    )
    Task_status = forms.ChoiceField(
        choices=[('', 'Select status')] + list(Tasks._meta.get_field('Task_status').choices),
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True,
        error_messages={'required': 'Please select a status.'}
    )

    class Meta:
        model = Tasks
        fields = ['title', 'description', 'duedate', 'priority', 'Task_status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'duedate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
