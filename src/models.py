from django.db import models

# Create your models here.

class Event(models.Model):

    def __str__(self):
        return self.author

    head = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField()
    content = models.CharField(max_length=2000)

class Upcoming_Event(models.Model):

    head = models.CharField(max_length=100)
    date = models.DateField()
    place = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
