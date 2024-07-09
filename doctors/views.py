from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorsListView(APIView):
    def get(self, request, department_id=None):
        if department_id:
            doctors = Doctor.objects.filter(departments_id=department_id)
        else:
            doctors = Doctor.objects.all()

        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)