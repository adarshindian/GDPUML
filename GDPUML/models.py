from django.db import models


# Create your models here.
class Signup(models.Model):
    uname = models.CharField(max_length=50)
    uemail = models.EmailField()
    upass = models.CharField(max_length=50)
    udate=models.DateField()

class Login(models.Model):
    uemail = models.EmailField()
    upass = models.CharField( max_length=50)

