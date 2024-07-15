from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import status
from .serializers import *

@api_view(['GET'])
def list_departments(request):
    departments = Departments.objects.all()
    serializer = DepartmentsSerializer(departments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_name(request):
    department_name = request.GET.get('name')
    if not department_name:
        return Response({'error': 'Department name is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        department = Departments.objects.get(departments_name=department_name)
        serializer = DepartmentsSerializer(department)
        return Response(serializer.data)
    except Departments.DoesNotExist:
        return Response({'error': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def department_locations_list(request):
    department_locations = DepartmentLocations.objects.all()
    serializer = DepartmentLocationsSerializer(department_locations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def department_locations_detail(request, department_id):
    department_locations = DepartmentLocations.objects.filter(departments_id=department_id)
    if not department_locations.exists():
        return Response({'error': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = DepartmentLocationsSerializer(department_locations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def floor_map_detail(request, floor):
    try:
        floor_map = FloorMap.objects.get(floor=floor)
        serializer = FloorMapSerializer(floor_map)
        return Response(serializer.data)
    except FloorMap.DoesNotExist:
        return Response({'error': 'Floor not found'}, status=status.HTTP_404_NOT_FOUND)