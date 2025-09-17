# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from users.forms import LoginForm, RegisterForm # import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages import get_messages

def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('tasks:listtasks')
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
        if user:
    # Clear any old messages
         list(get_messages(request))   #This clears the queue
         login(request, user)
         return redirect('tasks:listtasks')
        else:
                messages.error(request, 'Invalid username or password.')
                return render(request, 'users/login.html', {'form': form})
        
    messages.error(request, 'Invalid form submission.')
    return render(request, 'users/login.html', {'form': form})

def sign_out(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('users:login')

# Code for the signup function
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/signup.html', {'form': form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # ✅ Don't log in the user immediately
            messages.success(request, 'Registration successful. Please login now.')
            return redirect('users:login')  # ✅ Redirect to login page
        
        messages.error(request, 'Registration failed. Please correct the errors below.')
        return render(request, 'users/signup.html', {'form': form})

    
def home(request):
    return render(request, 'home.html')