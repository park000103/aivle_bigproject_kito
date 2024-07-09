from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('add/', views.add_patient, name='add_patient'),
    path('list/', views.patients_list, name='patients_list'),
    path('list2/', PatientListAPIView.as_view(), name='patient-list2'), # 전체환자 조회
    path('list2/search/', PatientSearchAPIView.as_view(), name='patient-search'), #이름과 생년월일로 조회 GET /patients/list2/search/?name=김환자&patient_bday=800101

    path('check_new_old', views.check_new_old),
    path('search_patient', views.search_patient),
    path('new_patient', views.new_patient),
    path('patient_list', views.patient_list),
    path('patient_list_page', views.patient_list_page),

]