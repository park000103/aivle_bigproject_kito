from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor
from .serializers import DoctorSerializer
import json

class DoctorsListView(APIView):
    def get(self, request, department_id=None):
        if department_id:
            doctors = Doctor.objects.filter(departments_id=department_id).select_related('departments_id').all()
        else:
            doctors = Doctor.objects.all()

        serializer = DoctorSerializer(doctors, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

def search_doctors(request):
    department = request.GET.get('doctor_depa')
    patient = request.GET.get('patient_id')

    doctors = Doctor.objects.filter(departments_id=department).select_related('departments_id').all()

    return render(request, 'doctors/doctor_list.html', {'doctors': doctors, 'patient': patient})

def doctor_list_page(request):

    json_data = request.GET.get('json_data', '{}')
    patient = request.GET.get('patient', ' ')
    patient_name = request.GET.get('patient_name', ' ')
    doctors = json.loads(json_data)

    return render(request, 'doctors/doctor_list.html', {'doctors': doctors, 'patient': patient, 'patient_name': patient_name})