from django.urls import path, include
from . import views
from .views import *

urlpatterns = [

    path('add/', views.add_patient, name='add_patient'),
    path('list/', views.patients_list, name='patients_list'),
    path('list2/', PatientListAPIView.as_view(), name='patient-list2'), # 전체환자 조회
    path('list2/search/', PatientSearchAPIView.as_view(), name='patient-search'), #이름과 생년월일로 조회 GET /patients/list2/search/?name=김환자&patient_bday=800101
    path('search/', patient_search_view, name='patient-search-view'),
    path('search/results/', search_patients, name='search-patients'),
    path('<int:patient_id>/reservations/', patient_reservations, name='patient-reservations'),
    path('reservations/<int:reservation_id>/change_status/', change_reservation_status, name='change-reservation-status'),
]

