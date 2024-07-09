from django.shortcuts import render

from .models import Reservation
from departments.models import Departments
from django.http import HttpResponse
import json

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
def reservations_list_page(request):
    print('reservations_list_page', request)
    json_data = request.GET.get('json_data', '{}')
    patient_id = request.GET.get('patient_id', '-1')
    reservations = json.loads(json_data)
    print('reservations_list_page', reservations)
    return render(request, 'reservations/reservations_list.html', {'reservations': reservations, 'patient_id': patient_id})

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
        
        return render(request, 'reservations/add_reservations.html', {'departments': depart, 'patient_id': patient_id})  