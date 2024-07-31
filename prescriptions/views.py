from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Prescription
from .serializers import PrescriptionSerializer
import json

def prescription(request):

    json_data = request.GET.get('json_data', '{}')
    prescription = json.loads(json_data)
    return render(request, 'payments/prescription.html', {'prescription':prescription})

@api_view(['GET'])
def prescription_detail(request, consultation_id):
    try:
        prescription = Prescription.objects.get(consultation_id=consultation_id)
        serializer = PrescriptionSerializer(prescription)
        return Response(serializer.data)
    except Prescription.DoesNotExist:
        return Response({'error': 'Prescription not found'}, status=status.HTTP_404_NOT_FOUND)