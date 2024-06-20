import datetime
from django.shortcuts import render


from .models import Project, Contact

#
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# for contact form
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
# @login_required
def signupuser(request):
    if request.method == "GET":
        return render(
            request, "portfolio/signupuser.html", {"form": UserCreationForm()}
        )
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(
                    request,
                    "portfolio/signupuser.html",
                    {"form": UserCreationForm(), "error": "Username already taken"},
                )
            # return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'message': 'User created successfully!'})
        else:
            return render(
                request,
                "portfolio/signupuser.html",
                {"form": UserCreationForm(), "error": "Passwords did not match"},
            )


# @login_required
def loginuser(request):
    if request.method == "GET":
        return render(
            request, "portfolio/loginuser.html", {"form": AuthenticationForm()}
        )
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "portfolio/loginuser.html",
                {
                    "form": AuthenticationForm(),
                    "error": "Username and password did not match",
                },
            )
        else:
            login(request, user)
            return redirect("home")


@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")


@login_required
def home(request):
    projects = Project.objects.all()
    return render(request, "portfolio/home.html", {"projects": projects})


# contact page
@login_required
def contact_me(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Additional validation can go here
            form.save()
            messages.success(request, " successfully sent! \n I will get back to you. ")
            return redirect("contact_me")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()
    return render(request, "portfolio/contact_me.html", {"form": form})
