from django.urls import path
from . import views
from .views import get_recommendation

urlpatterns = [
    path('recommend/', get_recommendation, name='get_recommendation'),
]
