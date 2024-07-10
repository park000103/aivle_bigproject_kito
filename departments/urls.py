from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('list/', views.list_departments, name='list_departments'),
    path('search_name/',search_name,name='search_name')
]
