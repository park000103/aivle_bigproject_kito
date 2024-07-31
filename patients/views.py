from datetime import date
from django.shortcuts import render, redirect
from .models import Patient
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PatientSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from reservations.models import Reservation
from reservations.serializers import ReservationSerializer

from django.http import HttpResponse
import json
from doctors.serializers import *
from departments.serializers import *
from django.utils import timezone

class PatientSearchAPIView(APIView):
    def get(self, request, format=None):
        # URL 쿼리 파라미터에서 이름과 생년월일(YYMMDD)을 가져옴
        name = request.query_params.get('name', None)
        bday = request.query_params.get('patient_bday', None)

        # 이름과 생일이 모두 제공되어야 함
        if not name or not bday:
            return Response({'error': '이름과 생년월일을 모두 입력하세요.'}, status=status.HTTP_400_BAD_REQUEST)

        # 이름과 생일로 환자를 찾음 (이름은 대소문자 구분 없이 검색)
        patients = Patient.objects.filter(patient_name__iexact=name, patient_bday=bday)
        
        if patients.exists():
            serializer = PatientSerializer(patients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': '일치하는 환자가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
class PatientListAPIView(APIView):
    def get(self, request, format=None):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def patient_reservations(request, patient_id):
    today = timezone.now().date()
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        return Response({"error": "Patient not found"}, status=404)
   
    reservations = Reservation.objects.filter(patient_id=patient_id, reservation_status__in=[0, 1], reservation_date__date=today).select_related('doctor_id')
    serialized_reservations = []

    for reservation in reservations:
        serialized_reservation = {
            "reservation_date": reservation.reservation_date,
            "patient_name": patient.patient_name,
            "patient_id": patient.id,
            "doctor_name": reservation.doctor_id.doctor_name,
            "departments_name": reservation.doctor_id.departments_id.departments_name,
            "reservation_status": reservation.reservation_status,
            "id": reservation.id
        }
        serialized_reservations.append(serialized_reservation)

    print(serialized_reservations)
    return Response(serialized_reservations) # 이부분은 원래 이랬나? 아니면 프론트에서 수정?

@csrf_exempt
@api_view(['POST'])
def change_reservation_status(request, reservation_id):
    try:
        reservation = Reservation.objects.get(pk=reservation_id)
    except Reservation.DoesNotExist:
        return Response({"error": "Reservation not found"}, status=404)

    status = request.data.get('status')
    if status is not None:
        reservation.reservation_status = status
        reservation.save()
        return Response({"success": "Reservation status updated successfully"})
    else:
        return Response({"error": "Invalid status value"}, status=400)

# page render view...

def new_nav(request):
    return render(request, 'patients/new_nav.html')

def recept(request):
    return render(request, 'patients/recept.html')

def recept_auth(request):
    return render(request, 'patients/recept_auth.html')

# 조회된 환자를 보여주기 위한 페이지 로드, json 데이터 전달
def recept_auth2_page(request):
    json_data = request.GET.get('json_data', '{}')
    patients = json.loads(json_data)
    print('recept_auth2_page : ', patients)
    return render(request, 'patients/recept_auth2.html', {'patients': patients})