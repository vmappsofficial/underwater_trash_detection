from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=100)

    gender = models.CharField(max_length=20)
    dob = models.DateField()
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    photo = models.CharField(max_length=250)
    USER=models.OneToOneField(User, on_delete=models.CASCADE)


class Issue_report(models.Model):
    photo = models.CharField(max_length=250)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateField()
    action = models.CharField(max_length=100)
    Registration = models.ForeignKey(Registration, on_delete=models.CASCADE)

class Review(models.Model):
    review = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    date = models.DateField()
    Registration = models.ForeignKey(Registration, on_delete=models.CASCADE)

class Notification(models.Model):
    date = models.DateField()
    notification = models.CharField(max_length=100)

class Upload(models.Model):
    uploaded_file = models.CharField(max_length=400)
    date = models.DateField()
    REGISTRATION = models.ForeignKey(Registration, on_delete=models.CASCADE)




