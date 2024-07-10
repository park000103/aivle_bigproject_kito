from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Consultation
from payments.models import Payment
from .serializers import ConsultationSerializer

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