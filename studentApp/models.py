from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10,default="Not Specified") 
    state = models.CharField(max_length=50,default="Unknown")
    password = models.CharField(max_length=100,default="Not Specified")
    agree = models.BooleanField(default=False)

    def __str__(self):
        return self.name

