from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(required= True, max_length=15, label='Title')
    description = forms.CharField(required= True,widget=forms.TextInput, max_length=100, label='Description')
    duedate = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    #duedate = forms.DateField(required= True,widget=forms.SelectDateWidget, label='Due Date')
    priority = forms.ChoiceField(required= True,choices=[('', 'All'), ('high', 'high') , ('medium', 'medium'),('low', 'low')], label='Priority')
    # status field is not included as it is set to 'Pending' by default in the view
    
