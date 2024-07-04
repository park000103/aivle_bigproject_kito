from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_patient, name='add_patient'),  # 환자 추가 페이지
    path('list/', views.patients_list, name='patients_list'),  # 환자 리스트 페이지
]
