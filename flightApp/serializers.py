from pyexpat import model
from rest_framework import serializers
from flightApp.models import Flight, Passanger, Reservation
import re

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"

    def validate_flightNumber(self, flightNumber):
        if(re.match("^[a-zA-Z0-9]*$", flightNumber)==None):
            raise serializers.ValidationError("Invalid flight Number, required Aph Numeric")
        return flightNumber
class PassangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passanger
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"