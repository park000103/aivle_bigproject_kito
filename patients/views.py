from datetime import date
from django.shortcuts import render
 
from django.shortcuts import render, redirect
from .models import Patient
 
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
