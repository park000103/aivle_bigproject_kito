from django.shortcuts import render

# Create your views here.
from patients.serializers import PatientSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Consultation
from payments.models import Payment
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from patients.models import Patient
from .models import Consultation
from .serializers import *
from datetime import datetime
from rest_framework.renderers import JSONRenderer

class ConsultationPaymentListView(APIView):
    def get(self, request, patient_id=None):
        today = timezone.now().date()
        
        if patient_id:
            consultations = Consultation.objects.filter(patient_id=patient_id, consultation_date__date=today)
        else:
            consultations = Consultation.objects.filter(consultation_date__date=today)
        
        consultations_payment = consultations.exclude(id__in=Payment.objects.values_list('consultation_id', flat=True))
        serializer = ConsultationSerializer(consultations_payment, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class ConsultationPayListView(APIView):
    def get(self, request, patient_id=None, format=None):
        # Payment 테이블에 있는 consultation_id로 필터링하여 Consultation 객체들을 가져옵니다.
        consultations = Consultation.objects.filter(id__in=Payment.objects.values('consultation_id').distinct())
        
        # 쿼리 매개변수로 시작 날짜와 종료 날짜를 가져옵니다.
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        # 날짜가 유효한 경우 기간 필터링을 적용합니다.
        if start_date and end_date:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d')
                end_date = datetime.strptime(end_date, '%Y-%m-%d')
                consultations = consultations.filter(date__range=(start_date, end_date))
            except ValueError:
                return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if patient_id:
            consultations = consultations.filter(patient_id=patient_id)
            
        serializer = ConsultationPaySerializer(consultations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

def search_patient_view(request):
    return render(request, 'consultations/search_patient.html')

@api_view(['GET'])
def patient_search_results(request):
    name = request.query_params.get('name')
    birth = request.query_params.get('birth')

    patients = Patient.objects.filter(patient_name=name, patient_birth=birth)
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def patient_consultations(request):
    patient_id = request.query_params.get('patient_id')
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    try:
        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        return Response({"error": "환자 정보를 찾을 수 없습니다."}, status=404)

    consultations = Consultation.objects.filter(
        patient_id=patient,
        consultation_date__range=[start_date, end_date]
    )
    if consultations.exists():
        serializer = ConsultationSerializer(consultations, many=True)
        return Response(serializer.data)
    else:
        return Response({"error": "해당 기간 내 진료 내역이 없습니다."}, status=404)

# def consultation_detail_view(request, consultation_id):
#     consultation = get_object_or_404(Consultation, id=consultation_id)
#     return render(request, 'consultations/consultation_detail.html', {'consultation': consultation})
def consultation_detail_view(request, consultation_id):
    consultation = get_object_or_404(Consultation, id=consultation_id)
    serializer = ConsultationPaySerializer(consultation)
    consultation_json = JSONRenderer().render(serializer.data)
    consultation_data = serializer.data  # Dictionary 형식으로도 데이터를 사용합니다.
    return render(request, 'consultations/consultation_detail.html', {'consultation': consultation_data})