from django.urls import path
from . import views

urlpatterns = [
    path('reservations_list', views.reservations_list),
    path('reservations_list_page', views.reservations_list_page),
    path('add_reservations', views.add_reservations),
]