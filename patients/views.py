from datetime import date
from django.shortcuts import render, redirect
from .models import Patient
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PatientSerializer
 
def add_patient(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        patient_birth = request.POST.get('patient_birth')
 
        # 날짜 형식을 YYYY-MM-DD로 변환
        patient_birth_date = date.fromisoformat(patient_birth)
 
        # 데이터베이스에 새 환자 추가
        patient = Patient(patient_name=patient_name, patient_birth=patient_birth_date)
        patient.save()
 
        return redirect('patients_list')  # 환자 리스트 페이지로 리다이렉트
    return render(request, 'patients/add_patient.html')
 
 
def patients_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patients_list.html', {'patients': patients}) #환자 조회 리스트

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