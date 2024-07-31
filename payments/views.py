from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from django.utils.dateparse import parse_date
from django.utils import timezone
from datetime import datetime, time

import json

class PaymentCreateAPIView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # 자동으로 현재 시간 저장됨
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentListAPIView(APIView):
    def get(self, request, patient_id=None):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        if patient_id:
            queryset = Payment.objects.filter(patient_id=patient_id)
        else:
            queryset = Payment.objects.all()

        if start_date and end_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            start_datetime = timezone.make_aware(datetime.combine(start_date, time.min), timezone.get_current_timezone())
            end_datetime = timezone.make_aware(datetime.combine(end_date, time.max), timezone.get_current_timezone())
            queryset = queryset.filter(payment_date__range=(start_datetime, end_datetime))

        serializer = PaymentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
def payment_patient_search(request):

    return render(request, 'payments/payment_patient_search.html')

def consultations_payment(request):

    consultation_id = request.GET.get('consultation_id', '0')
    return render(request, 'payments/consultations_payment.html', {'consultation_id': consultation_id})

def payment_patient_list(request):
    json_data = request.GET.get('json_data', '{}')
    patient_name = request.GET.get('patient_name', ' ')
    patients = json.loads(json_data)

    return render(request, 'payments/payment_patient_list.html', {'patients': patients, 'patient_name': patient_name}) 

def consultations_payment_list(request):
    json_data = request.GET.get('json_data', '{}')
    patient_name = request.GET.get('patient_name', ' ')
    payments = json.loads(json_data)

    return render(request, 'payments/consultations_payment_list.html', {'payments': payments, 'patient_name': patient_name}) 