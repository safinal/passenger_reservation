from django.urls import path
from .views import train_reservation, get_ticket, my_trips

urlpatterns = [
    path('', train_reservation),
    path('<int:trip_id>/', get_ticket),
    path('my_trips/', my_trips),
]
