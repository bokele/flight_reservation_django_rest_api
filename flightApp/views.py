from django.shortcuts import render
from flightApp.models import Flight, Passanger, Reservation
from flightApp.serializers import FlightSerializer, PassangerSerializer, ReservationSerializer
from rest_framework import viewsets

# Create your views here.

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassangerViewSet(viewsets.ModelViewSet):
    queryset = Passanger.objects.all()
    serializer_class = PassangerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

