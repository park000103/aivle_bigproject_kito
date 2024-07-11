from django.urls import path
from . import views
from .views import DoctorsListView

urlpatterns = [
    path('search_doctors', views.search_doctors),
    path('doctor_list_page', views.doctor_list_page),
    
    path('list/', DoctorsListView.as_view(), name='doctors-list'),
    path('list/<int:department_id>/', DoctorsListView.as_view(), name='doctors-by-department'),
]
