from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import RegisterForm, Login
# Create your views here.


def register(request):
    fd = RegisterForm()
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "username is used.")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is Used.")
            else:
                user = User.objects.create_user(
                    username=uname, first_name=fname, last_name=lname, email=email, password=password1)
                user.save()
                messages.info(request, "User is created.")
        else:
            messages.info(request, "Password is not matching...")

    return render(request, "account/register.html", {"fd": fd})


def login(request):
    fd = Login()
    if request.method == "POST":
        uname = request.POST['uname']
        password1 = request.POST['password1']
        user = auth.authenticate(username=uname, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("login")

    return render(request, "account/login.html", {"fd": fd})


def logout(request):
    auth.logout(request)
    return redirect('/')
