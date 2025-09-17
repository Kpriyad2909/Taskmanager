# New forms.py
from django import forms
from .models import Tasks

class TasksInputForm(forms.ModelForm):
    priority = forms.ChoiceField(
        choices=[('', 'Select priority')] + list(Tasks._meta.get_field('priority').choices),
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True,
        error_messages={'required': 'Please select a priority.'}
    )
    
    status = forms.ChoiceField(
        # Reference the 'status' field from the model, not a redundant name
        choices=[('', 'Select status')] + list(Tasks._meta.get_field('status').choices),
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True,
        error_messages={'required': 'Please select a status.'}
    )
    
    class Meta:
        model = Tasks
        # Use the single, correct field name 'status' in the fields list
        fields = ['title', 'description', 'duedate', 'priority', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'duedate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class Filters(forms.Form):
    search = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Search...', 'class': 'search-input'})
    )

    status = forms.ChoiceField(
        required=False,
        label='Status',
        choices=[('', 'All')] + list(Tasks.STATUS_CHOICES),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    priority = forms.ChoiceField(
        required=False,
        label='Priority',
        choices=[('', 'All')] + list(Tasks.PRIORITY_CHOICES), # Make sure you have this in your model
        widget=forms.Select(attrs={'class': 'form-select'})
    )
