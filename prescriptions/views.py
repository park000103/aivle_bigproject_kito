from django.shortcuts import render
from .models import Prescription

# Create your views here.

def prescription(request):
    print(request)
    consultation_id = request.GET.get('consultation_id', '0')
    print(consultation_id)
    queryset = Prescription.objects.filter(consultation_id=consultation_id)
    print(queryset)
    return render(request, 'payments/prescription.html', {'prescription':queryset})