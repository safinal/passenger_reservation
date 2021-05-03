from django.urls import path
from .views import train_reservation, get_ticket

urlpatterns = [
    path('', train_reservation),
    path('get-ticket/', get_ticket)
]
