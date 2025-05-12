from django.db import models


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=300)
    max_attendees = models.IntegerField()


class Attendee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event')
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, related_name='attendeee')
