# Create your models here.
from django.db import models


class User(models.Model):
    active = models.BooleanField()
    availability = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    experience = models.IntegerField(default=0)
    full_name = models.CharField(max_length=100)
    languages = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    rate = models.IntegerField(default=0)
    # resume = models.FileField(upload_to='documents')
    role = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
