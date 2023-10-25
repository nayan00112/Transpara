from django.shortcuts import render
from Blogs.models import FeedbackData
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def SuperUserInterface(request):
    # user list, delete option (also cleane history)
    # userdetails
    # superuser details
    
    # feedback form visite
    m = "Not avaliable!"

    

    if request.user.is_authenticated:
        # if User.objects.filter(is_superuser) == True:
        if request.user.is_superuser:

            if request.method == "POST":
                try:
                    de = request.POST["delete"]
                    print(de)
                    FeedbackData.objects.get(id = de[7:]).delete()
                except:
                    # messages.error(request, "Error: Not deleted")
                    pass

                try:
                    ch =request.POST["checked"]
                    a = FeedbackData.objects.get(id = ch[8:])
                    a.status = True
                    print(request.user.username)
                    a.checkers_superuser = request.user.username
                    print("Dddd")
                    a.save()

                except:
                    # messages.error(request, "Error: not checked")
                    pass
                
            fm = FeedbackData.objects.all()
            return render(request, "superuser/mainpage.html", {"fm":fm})

    return render(request, "superuser/mainpage.html", {"m":m})