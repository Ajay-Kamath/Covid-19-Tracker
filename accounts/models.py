from django.db import models

# Create your models here.
class Patients(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phonenumber = models.BigIntegerField()
    age = models.BigIntegerField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    travelhistory = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

