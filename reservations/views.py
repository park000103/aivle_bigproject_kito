from .models import Reservation
from departments.models import Departments
from django.http import HttpResponse

from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .km_bert_model import specialty_predict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReservationCreateSerializer
from datetime import datetime

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
            print(reservation)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def add_reservation(request):
    patient_id = request.GET.get('patient_id')
    if not patient_id:
        return redirect('patient_check')
    return render(request, 'reservations/add_reservations.html', {'patient_id': patient_id})

# Create your views here.
def reservations_list(request):
    # reserv = Reservation.objects.all()
    # print(request.POST)
    # print(request.POST.get('selected_patient'))
    print(request.GET)
    print(request.GET.get('selected_patient'))
    # print(type(request.POST.get('selected_patient')))
    # a = request.POST.get('selected_patient', 0)
    a = request.GET.get('selected_patient', 0)
    print(a)
    reserv = Reservation.objects.filter(patient_id=int(a))
    print(reserv)
    
    # json 형식으로 맞추는 과정
    reserv_data = list(reserv.values('id', 'reservation_date', 'patient_id', 'doctor_id', 'reservation_status'))
    
    for reserv in reserv_data:
        reserv['reservation_date'] = reserv['reservation_date'].isoformat() if reserv['reservation_date'] else None
    
    json_data = json.dumps(reserv_data)
    print("json_data!!" ,json_data)
    # content_type을 명시하기 위한 과정
    response = HttpResponse(json_data, content_type='application/json')
    return response
    # return render(request, 'reservations/reservations_list.html', {'reservations': reserv, 'patient_id': a})

# 조회된 예약을 보여주기 위한 페이지 로드, json 데이터 전달
def reserve(request):
    print('reserve', request)
    json_data = request.GET.get('json_data', '{}')
    patient_id = request.GET.get('patient_id', '-1')
    reservations = json.loads(json_data)
    reservations = [parse_reservation_date(reservation) for reservation in reservations]
    print(reservations)
    return render(request, 'reservations/reserve.html', {'reservations': reservations, 'patient_id': patient_id})

def parse_reservation_date(reservation):
    reservation['reservation_date'] = datetime.fromisoformat(reservation['reservation_date'].rstrip('Z'))
    print('시간 변경! : ', reservation)
    return reservation

def add_reservations(request):
    if request.method == 'POST':
        test = request.POST
        print(test)
        print(test.get('patient_id'))
        return render(request, 'index.html')
    else :
        depart = Departments.objects.all()
        print(depart)
        patient_id = request.GET.get('patient_id')
        # json_data = request.GET.get('json_data', '{}')
        # patient_id = json.loads(json_data)
        print('~~~~~~~~~~~~~~~~~~~~~~')
        print('request', request.GET)
        print('patient_id', patient_id)
        
        return render(request, 'reservations/make_res.html', {'departments': depart, 'patient_id': patient_id})  