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

#

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

# 이름, 생년월일로 환자 조회
def recept_auth2(request):
    print(request)
    if request.method == 'POST':
    # POST 요청에 대한 처리
    # request.POST를 사용하여 데이터 처리
        print('POST!!!')
        print('request data : ',request.POST.get('patient_name'))
        pass
    else:
    # GET 요청에 대한 처리 (옵션)
        print('GET!!!')
        # print(request.GET)
        # print(request.GET[0])
        # print(request.GET.get('name', ''))
        # print(request.GET.get('birth', ''))
        pass
    print('여기까지 나옴0')
    # 조건에 맞는 환자 조회
    print(request.GET)
    js = request.GET.getlist('json_data')
    
    if js:
        json_data_str = js[0]  # 리스트의 첫 번째 요소를 가져옴
        json_data_list = json.loads(json_data_str)  # JSON 문자열을 파이썬 리스트로 변환

        if json_data_list:
            for item in json_data_list:
                patient_name = item.get('patient_name')
                patient_birth = item.get('patient_birth')
            
    #people = Patient.objects.filter(patient_name=request.GET.get('patient_name'),
    #                                patient_birth=request.GET.get('patient_birth'))
    people = Patient.objects.filter(patient_name=patient_name,
                                    patient_birth=patient_birth)
    
    print('여기까지 나옴1')
    if people :
        print(people)
        print('여기까지 나옴2')
        print(people[0].id)
        print(people[0].patient_name)

        # json 형식으로 맞추는 과정
        patients_data = list(people.values('id', 'patient_name', 'patient_birth'))
        
        for peo in patients_data:
            peo['patient_birth'] = peo['patient_birth'].isoformat() if peo['patient_birth'] else None
        
        json_data = json.dumps(patients_data)
        print("json_data!!" ,json_data)
        # content_type을 명시하기 위한 과정
        response = HttpResponse(json_data, content_type='application/json')
        return response
        # return render(request, 'patients\patient_list.html', {'patients': json_data})
    else :
        return render(request, 'patients/new_nav.html')
#
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
    
# 검색 폼을 렌더링하는 뷰
def patient_search_view(request):
    return render(request, 'patients/patient_search.html')

@api_view(['GET'])
def search_patients(request):
    name = request.GET.get('name')
    birth = request.GET.get('birth')
    print(birth)
    patients = Patient.objects.filter(patient_name__exact=name, patient_birth=birth)
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def patient_reservations(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        return Response({"error": "Patient not found"}, status=404)

    reservations = Reservation.objects.filter(patient_id=patient_id, reservation_status__in=[0, 1]).select_related('doctor_id')
    serialized_reservations = []
    for reservation in reservations:
        serialized_reservation = {
            "reservation_date": reservation.reservation_date,
            "patient_name": patient.patient_name,
            "doctor_name": reservation.doctor_id.doctor_name,
            "reservation_status": reservation.reservation_status,
            "id": reservation.id
        }
        serialized_reservations.append(serialized_reservation)
    return Response(serialized_reservations)

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
