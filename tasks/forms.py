from django import forms
from .models import Tasks

class TasksInputForm(forms.ModelForm):
    priority = forms.ChoiceField(
        choices=[('', 'Select priority')] + list(Tasks._meta.get_field('priority').choices),
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True,
        error_messages={'required': 'Please select a priority.'}
    )
<<<<<<< HEAD
    Task_status = forms.ChoiceField(
        choices=[('', 'Select status')] + list(Tasks._meta.get_field('Task_status').choices),
=======
    completed = forms.ChoiceField(
        choices=[('', 'Select status')] + list(Tasks._meta.get_field('completed').choices),
>>>>>>> 243e48f1faac87284f54b9eda3acb04c14e4f464
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True,
        error_messages={'required': 'Please select a status.'}
    )

    class Meta:
        model = Tasks
<<<<<<< HEAD
        fields = ['title', 'description', 'duedate', 'priority', 'Task_status']
=======
        fields = ['title', 'description', 'duedate', 'priority', 'completed']
>>>>>>> 243e48f1faac87284f54b9eda3acb04c14e4f464
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'duedate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
