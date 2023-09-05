from django.db import models

# Create your models here.


class UserData(models.Model):
    user_id = models.CharField(max_length=10)
    user_data = models.TextField()
    dateandtime = models.CharField(max_length=30)
