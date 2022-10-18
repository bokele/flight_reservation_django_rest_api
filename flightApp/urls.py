
from django.urls import path,include
from flightApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("flights", views.FlightViewSet)
router.register("passangers", views.PassangerViewSet)
router.register("reservations", views.ReservationViewSet)

urlpatterns = [
    path("", include(router.urls) ),
path("find/flights/", views.find_flights)
path("reservations/store/", views.store_reservation)
]
