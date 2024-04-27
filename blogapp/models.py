from django.db import models
from django.contrib import admin
class signupdetails(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
# Create your models here.
class postdetails(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=10000)
    image=models.ImageField(upload_to='images',default='')

class contactdetails(models.Model):
 name = models.CharField(max_length=100)
 email = models.CharField(max_length=50)
 contactno = models.BigIntegerField()
 message=models.CharField(max_length=10000)
