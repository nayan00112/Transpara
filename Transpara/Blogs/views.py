from django.shortcuts import render
from .forms import FeedBackForm
from .models import FeedbackData
from django.contrib import messages
from datetime import datetime


# Create your views here.

def about(request):
    return render (request, "Blogs/about.html", {"active_about":"active"})


def contact(request):
    fm = FeedBackForm()
    if request.method=="POST":
        if request.user.is_authenticated:
            try:
                topic_title = request.POST['topic_title']
                email = request.user.email
                feedbackmessage = request.POST['feedbackmessage']
                # day month year Hour Minute Second
                dateandtime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                fd = FeedbackData(topic_title = topic_title, email = email, feedbackmessage = feedbackmessage, currenttime = dateandtime, status = False)
                fd.save()
                messages.info(request, "Responce saved successfully.")
            except:
                messages.error(request, "Error: Not saved responce!")
        else:
            messages.error(request, "<p style='color:red;'>Login required!</p>")
    if request.user.is_authenticated:
        return render (request, "Blogs/contact.html", {"active_contact":"active", 'fm' :fm})
    else:
        return render (request, "Blogs/contact.html")

