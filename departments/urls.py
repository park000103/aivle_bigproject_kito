from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('list/', views.list_departments, name='list_departments'),
    path('search_name/',search_name,name='search_name'),
    path('department-locations/', department_locations_list, name='department_locations_list'),
    path('department-locations/<int:department_id>/', department_locations_detail, name='department_locations_detail'),
    path('floor-map/<int:floor>/', floor_map_detail, name='floor_map_detail'),
]
