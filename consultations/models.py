from django.db import models
from doctors.models import Doctor
from reservations.models import Reservation
from patients.models import Patient

# Create your models here.
class Consultation(models.Model): #진료
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor_id =models.ForeignKey(Doctor,on_delete=models.CASCADE)
    consultation_date = models.DateTimeField(auto_now=True)
    amount = models.IntegerField()
    reservation_id = models.ForeignKey(Reservation,on_delete=models.CASCADE)
    description = models.TextField()
    class Meta:
        db_table = "consultation"
        verbose_name = "진료"

class DetailConsultation(models.Model): # 세부진료
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    consultation_id = models.ForeignKey(Consultation,on_delete=models.CASCADE)
    class Meta:
        db_table = "detail_consultation"
        verbose_name = "세부진료"