from django.urls import path
from .views import DoctorsListView

urlpatterns = [
    path('list/', DoctorsListView.as_view(), name='doctors-list'),
    path('list/<int:department_id>/', DoctorsListView.as_view(), name='doctors-by-department'),
]