from django.db import models

# Create your models here.

class Event(models.Model):

    def __str__(self):
        return self.author

    # def save(self, *args, **kwargs):
    #     super(Event, self).save(*args, **kwargs)

    head = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField()
    content = models.CharField(max_length=2000)

class Upcoming_Event(models.Model):

    head = models.CharField(max_length=100)
    date = models.DateField()
    place = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)

class Finance(models.Model):

    date = models.DateField()
    amount_exp = models.IntegerField()

    def yearpublished(self):
        return self.date.strftime('%Y')

    def monthpublished(self):
        return self.date.strftime('%B')

    
    # def save(self, *args, **kwargs):
    #     super(Finance, self).save(*args, **kwargs)


