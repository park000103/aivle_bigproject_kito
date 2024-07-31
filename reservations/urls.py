from django.urls import path
from . import views
from .views import *

app_name = 'reservations'

urlpatterns = [
    path('add/', views.add_reservation, name='add_reservation'),
    path('recommend/', get_recommendation, name='get_recommendation'),
    path('create/', ReservationCreateAPIView.as_view(), name='reservation-create'), # 환자 예약 생성

    path('reservations_list', views.reservations_list),
    path('reserve', views.reserve), # 환자 예약 목록 page
    path('add_reservations', views.add_reservations), # 과 선택 or 증상 별 과 추천
]