from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .km_bert_model import specialty_predict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import localtime
from datetime import datetime
from .models import Reservation
from .serializers import ReservationCreateSerializer


@csrf_exempt
def get_recommendation(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            user_symptom = body.get('symptom')
            if not user_symptom:
                return JsonResponse({'error': 'No symptom provided'}, status=400)

            departments, probs = specialty_predict(user_symptom)
            response = {
                'recommended_departments': departments.split(', '),
                'probabilities': probs.tolist()
            }
            return JsonResponse(response)
        except Exception as e:
            import traceback
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

class ReservationCreateAPIView(APIView):
    def post(self, request):
        serializer = ReservationCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            patient_id = serializer.validated_data['patient_id']
            doctor_id = serializer.validated_data['doctor_id']
            
            # 현재 시간을 가져옵니다.
            current_time = datetime.now()
            
            # 오늘의 오후 6시를 계산합니다.
            reservation_date = datetime(current_time.year, current_time.month, current_time.day, 18, 0, 0)
            
            # 예약 객체 생성
            reservation = Reservation(
                patient_id=patient_id,
                doctor_id=doctor_id,
                reservation_date=reservation_date,
                reservation_status=1  # 대기중으로 설정
            )
            reservation.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def add_reservation(request):
    patient_id = request.GET.get('patient_id')
    if not patient_id:
        return redirect('patient_check')
    return render(request, 'reservations/add_reservation.html', {'patient_id': patient_id})