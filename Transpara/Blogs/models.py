from django.db import models

# Create your models here.

class FeedbackData(models.Model):
    email = models.EmailField(max_length=254)
    feedbackmessage = models.TextField()
