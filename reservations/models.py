from django.db import models
# Create your models here.
from doctors.models import Doctor
from patients.models import Patient
class Reservation(models.Model): #예약
    RESERVATION_STATUS_CHOICES = (
        (0, '예약됨'),
        (1, '대기중'),
        (2, '완료'),
        (3, '불참'),
    )
    
    reservation_date = models.DateTimeField(verbose_name="예약 날짜")
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE,verbose_name="환자이름")
    doctor_id =models.ForeignKey(Doctor,on_delete=models.CASCADE,verbose_name="의사")
    reservation_status = models.IntegerField(choices=RESERVATION_STATUS_CHOICES,verbose_name="예약 상태")
    
    def __str__(self):
        return f"{self.patient_id} - {self.doctor_id} ({self.get_reservation_status_display()})"
    
    class Meta:
        db_table = "reservation"
        verbose_name = "예약"
        verbose_name_plural = "예약들"