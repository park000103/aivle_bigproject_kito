from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Departments
from rest_framework import status
from .serializers import DepartmentsSerializer

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