from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('list2/', PatientListAPIView.as_view(), name='patient-list2'), # 전체환자 조회
    path('list2/search/', PatientSearchAPIView.as_view(), name='patient-search'), #이름과 생년월일로 조회 GET /patients/list2/search/?name=김환자&patient_bday=800101

    path('<int:patient_id>/reservations/', patient_reservations, name='patient-reservations'),
    path('reservations/<int:reservation_id>/change_status/', change_reservation_status, name='change-reservation-status'),

    path('new_nav', views.new_nav), # 신규 환자 원무과 안내 page
    path('recept', views.recept),   # 신규, 기존 환자 구분 page
    path('recept_auth', views.recept_auth), # 환자 검색 page
    path('recept_auth2_page', views.recept_auth2_page), # 검색 된 환자 목록 page
]