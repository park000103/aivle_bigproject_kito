from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from django.utils.dateparse import parse_date
from django.utils import timezone

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

        if start_date:
            start_date = parse_date(start_date)
            queryset = queryset.filter(payment_date__gte=start_date)
        if end_date:
            end_date = parse_date(end_date)
            queryset = queryset.filter(payment_date__lte=end_date)

        serializer = PaymentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)