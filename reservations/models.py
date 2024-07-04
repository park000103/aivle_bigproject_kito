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
    
    reservation_date = models.DateTimeField()
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor_id =models.ForeignKey(Doctor,on_delete=models.CASCADE)
    reservation_status = models.IntegerField(choices=RESERVATION_STATUS_CHOICES)
    class Meta:
        db_table = "reservation"
        verbose_name = "예약"