from django.db import models

# Create your models here.


class UserData(models.Model):
    user_name = models.CharField(max_length=50)
    user_data = models.TextField()
    dateandtime = models.CharField(max_length=30)
