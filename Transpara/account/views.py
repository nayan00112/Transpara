from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import RegisterForm, Login
from django.http import Http404, HttpResponse

# Create your views here.


def register(request):
    fd = RegisterForm()
    if request.method == "POST":
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = request.POST['username']
        password1 = request.POST['create_password1']
        password2 = request.POST['conform_password2']
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

    return render(request, "account/register.html", {"fd": fd, "active_register":"active"})


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

    return render(request, "account/login.html", {"fd": fd, "active_login":"active"})


def logout(request):
    auth.logout(request)
    return redirect('/')


def myprofile(request):
    if request.user.is_authenticated:
        # print(request.user)
        return render(request, "profile/myprofile.html", {"active_myprofile":"active"})
    else:
        return Http404


def editprofile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            uid = request.POST['user_id']
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            uname = request.POST['uname']
            email = request.POST['email']
            cpassword = request.POST['cpassword']
            npassword = request.POST['npassword']

            user = auth.authenticate(username=request.user, password=cpassword)
            print(user)
            if user is not None:

                if User.objects.filter(username=uname).exists() and str(User.objects.filter(username=uname).first().id) != str(request.user.id):
                    print(User.objects.filter(username=uname).exists() , str(User.objects.filter(username=uname).first().id) , str(request.user.id))
                    messages.info(request, "Username is already taken.")
                elif User.objects.filter(email=email).exists() and str(User.objects.filter(email=email).first().id) != str(request.user.id):
                    print(User.objects.filter(email=email).exists() , User.objects.filter(email=email).first().id , str(request.user.id))
                    messages.info(request, "Email is already taken.")
                else:
                    user.username = uname
                    user.first_name = fname
                    user.last_name = lname
                    user.email = email
                    user.set_password(npassword)
                    user.save()
                    auth.logout(request)
                    messages.info(request, "updated successfully and logout.")
            else:
                messages.info(request, "Invalid credential")

        return render(request, "profile/editprofile.html", {"active_editprofile":"active"})
    else:
        return HttpResponse(request, "Not Found")
