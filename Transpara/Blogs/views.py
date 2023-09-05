from django.shortcuts import render

# Create your views here.

def about(request):
    return render (request, "Blogs/about.html", {"active_about":"active"})

def contact(request):
    return render (request, "Blogs/contact.html", {"active_contact":"active"})

