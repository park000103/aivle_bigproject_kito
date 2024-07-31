from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('list/', views.list_departments, name='list_departments'),
    path('search_name/', search_name, name='search_name'),
    path('department-locations/', department_locations_list, name='department_locations_list'),
    path('department-locations/<int:department_id>/', department_locations_detail, name='department_locations_detail'),
    path('floor-map/<int:floor>/', floor_map_detail, name='floor_map_detail'),
    path('floor_map/', floor_map, name='floor_map'),
    path('map_search/', map_search, name='map_search'), # 해당 과로 이동하는 경로 지도 표시
    path('floor_map/search_page/', floor_map_search_page, name='floor_map_search_page'),
    path('floor_keyboard/', floor_keyboard, name='floor_keyboard'),
    path('floor-map/search/', floor_map_search, name='floor_map_search'),
]