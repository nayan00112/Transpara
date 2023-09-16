from django.shortcuts import render
from .forms import FeedBackForm
from .models import FeedbackData
from django.contrib import messages


# Create your views here.

def about(request):
    return render (request, "Blogs/about.html", {"active_about":"active"})


def contact(request):
    fm = FeedBackForm()
    if request.method=="POST":
        try:
            email = request.POST['email']
            feedbackmessage = request.POST['feedbackmessage']
            fd = FeedbackData(email = email, feedbackmessage = feedbackmessage)
            fd.save()
            messages.info(request, "Responce saved successfully.")
        except:
            messages.error(request, "Error: Not saved responce!")
        
    return render (request, "Blogs/contact.html", {"active_contact":"active", 'fm' :fm})

