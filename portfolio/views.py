from django.shortcuts import render
from .models import Project
#
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
# Create your views here.

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'portfolio/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'portfolio/signupuser.html', {'form': UserCreationForm(), 'error': 'Username already taken'})
            # return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'message': 'User created successfully!'})
        else:
            return render(request, 'portfolio/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'portfolio/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'portfolio/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')
        

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

