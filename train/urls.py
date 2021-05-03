from django.urls import path
from .views import train_reservation

urlpatterns = [
    path('', train_reservation),
]
