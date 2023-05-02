from django.db import models

class internship(models.Model):

    name = models.CharField(max_length=100)
    college = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    phone = models.IntegerField()
    experience = models.IntegerField()
    Subject = models.CharField(max_length=50)