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
        print('의사다~ : ',doctors)
        serializer = DoctorSerializer(doctors, many=True)
        print('직렬화~ : ', serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

def search_doctors(request):
    department = request.GET.get('doctor_depa')
    patient = request.GET.get('patient_id')
    print('-------------------')
    print(request)
    print(department)
    print(patient)
    doctors = Doctor.objects.filter(departments_id=department).select_related('departments_id').all()
    print(doctors)
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors, 'patient': patient})

def doctor_list_page(request):
    print(request)
    json_data = request.GET.get('json_data', '{}')
    patient = request.GET.get('patient', ' ')
    doctors = json.loads(json_data)
    print('의사 목록이다~! : ', doctors)
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors, 'patient': patient})