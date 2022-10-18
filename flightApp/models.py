from django.db import models

# Create your models here.

class Flight(models.Model):
    flifhtNumber = models.CharField(max_length=10)
    operationAirlines = models.CharField(max_length=100)
    departtureCity = models.CharField(max_length=100)
    arrialCity = models.CharField(max_length=100)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()
    createdAt = models.DateTimeField(now=True, blank=True)
    updatedAt = models.DateTimeField(now=True, blank=True)


class Passanger(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    createdAt = models.DateTimeField(now=True, blank=True)
    updatedAt = models.DateTimeField(now=True, blank=True)

class Reservation(models.Model):
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE)
    passanger = models.OneToOneField(Passanger, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(now=True, blank=True)
    updatedAt = models.DateTimeField(now=True, blank=True)