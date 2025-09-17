# users/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Form for logging in with username and password
class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'})
    )
    password = forms.CharField(
        max_length=63,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'})
    )

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter First name'})
    )
    last_name = forms.CharField(
        max_length=150, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter Last name'})
    )
    email = forms.EmailField(
        max_length=150, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        # This is the corrected field order
        fields = ('first_name', 'last_name', 'username','email') + UserCreationForm.Meta.fields[1:]
        
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
        }
