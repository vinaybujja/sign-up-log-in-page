from django.db import models


# Create your models here.
class registration(models.Model):
    username = models.CharField(max_length=100, default='unknown', primary_key=True)
    firstname = models.CharField(max_length=100, default='unknown')
    lastname = models.CharField(max_length=100, default='unknown')
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

