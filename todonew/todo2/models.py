from django.db import models

# Create your models here.


class Tasks(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default =False)
    created = models.DateTimeField(auto_now_add=True)


class Register(models.Model):
    username = models.CharField(max_length=150, blank=True)
    email= models.EmailField(max_length=150, blank=True)
    password = models.CharField(max_length=150, blank=True)


class Login(models.Model):
    username = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=150, blank=True)

