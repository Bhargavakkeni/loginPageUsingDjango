from django.db import models

# Create your models here.
class LoginDetails(models.Model):
    username = models.CharField(max_length=255) #creates a column in database
    password = models.CharField(max_length=8)