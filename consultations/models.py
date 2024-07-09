from django.db import models
from doctors.models import Doctor
from reservations.models import Reservation
from patients.models import Patient

# Create your models here.
class Consultation(models.Model): #진료
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE, verbose_name="환자")
    doctor_id =models.ForeignKey(Doctor,on_delete=models.CASCADE, verbose_name="의사")
    consultation_date = models.DateTimeField(auto_now=True, verbose_name="진료날짜")
    amount = models.IntegerField( verbose_name="금액")
    reservation_id = models.ForeignKey(Reservation,on_delete=models.CASCADE, verbose_name="예약번호")
    description = models.TextField( verbose_name="설명")
    def __str__(self):
        return f"{self.patient_id} - {self.doctor_id} - {self.consultation_date}"
    
    class Meta:
        db_table = "consultation"
        verbose_name = "진료"
        verbose_name_plural = "진료들"
        

class DetailConsultation(models.Model): # 세부진료
    name = models.CharField(max_length=200, verbose_name="세부 진료명")
    amount = models.IntegerField(verbose_name="금액")
    consultation_id = models.ForeignKey(Consultation,on_delete=models.CASCADE, verbose_name="진료번호")
    class Meta:
        db_table = "detail_consultation"
        verbose_name = "세부진료"
        verbose_name_plural = "세부진료들"