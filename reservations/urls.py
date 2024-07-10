from django.urls import path
from . import views
from .views import *

app_name = 'reservations'

urlpatterns = [
    path('add/', views.add_reservation, name='add_reservation'),
    path('recommend/', get_recommendation, name='get_recommendation'),
    path('create/', ReservationCreateAPIView.as_view(), name='reservation-create'),
]
