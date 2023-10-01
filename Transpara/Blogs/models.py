from django.db import models

# Create your models here.

class FeedbackData(models.Model):
    topic_title = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    feedbackmessage = models.TextField()
    currenttime = models.DateField(auto_now=True, auto_now_add=False)
    status = models.BooleanField()
