from django.urls import path
from . import views
from .views import prescription_detail

urlpatterns = [
    path('prescription/<int:consultation_id>/', prescription_detail, name='prescription_detail'),
]