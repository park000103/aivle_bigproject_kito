from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('add/', views.add_patient, name='add_patient'),
    path('list/', views.patients_list, name='patients_list'),
    path('list2/', PatientListAPIView.as_view(), name='patient-list2'),
    path('list2/search/', PatientSearchAPIView.as_view(), name='patient-search'),
]