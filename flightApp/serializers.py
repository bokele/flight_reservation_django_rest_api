from pyexpat import model
from rest_framework import serializers
from flightApp.models import Flight, Passanger, Reservation


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all_"

class PassangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passanger
        fields = "__all_"

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all_"