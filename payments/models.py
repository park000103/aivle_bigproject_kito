from django.db import models
from consultations.models import Consultation
from patients.models import Patient
# Create your models here.
class Payment(models.Model): #수납
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE,verbose_name="환자")
    payment_date = models.DateTimeField(auto_now_add=True,verbose_name="결제 날짜")
    amount = models.IntegerField(verbose_name="금액")
    payment_method = models.CharField(max_length=50,verbose_name="결제방법")
    consultation_id = models.ForeignKey(Consultation,on_delete=models.CASCADE,verbose_name="진료번호")
    class Meta:
        db_table ="payment"
        verbose_name = "수납"
        verbose_name_plural = "수납"
    def __str__(self):
        return f"{self.patient_id} - {self.amount}원"
              
