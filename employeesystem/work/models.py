from django.db import models

class Employee(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    address_pincode = models.CharField(max_length=70, default="")
    address_state = models.CharField(max_length=50)
    address_city = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
