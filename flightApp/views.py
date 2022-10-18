from django.shortcuts import render
from flightApp.models import Flight, Passanger, Reservation
from flightApp.serializers import FlightSerializer, PassangerSerializer, ReservationSerializer
from rest_framework import viewsets

# Create your views here.


