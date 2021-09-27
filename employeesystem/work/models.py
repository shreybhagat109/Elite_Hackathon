from django.db import models

class Employee(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    pincode = models.CharField(max_length=70, default="")
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

def __str__(self):
    return self.first_name