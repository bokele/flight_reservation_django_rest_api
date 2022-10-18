from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.

class Flight(models.Model):
    flifhtNumber = models.CharField(max_length=10)
    operationAirlines = models.CharField(max_length=100)
    departtureCity = models.CharField(max_length=100)
    arrialCity = models.CharField(max_length=100)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True)


class Passanger(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True)

class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passanger = models.OneToOneField(Passanger, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)