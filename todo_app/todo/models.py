from django.db import models

# Create your models here.


class Tasks(models.Model):  # Register is the classname or table name
    title = models.CharField(max_length=150)
    # description = models.TextField(blank=True)
    completed = models.BooleanField(default =False)  # completed enna condition true aaya matram value true aavum
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # idhu oru extra string field nu vendi ulla constructor or fn
        return self.title


class Register(models.Model):
    username = models.CharField(max_length=150, blank=True)
    email= models.EmailField(max_length=150, blank=True)
    password = models.CharField(max_length=150, blank=True)


class Login(models.Model):
    username = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=150, blank=True)
