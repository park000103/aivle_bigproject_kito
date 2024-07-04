from django.db import models
from consultations.models import Consultation
from patients.models import Patient
# Create your models here.
class Payment(models.Model): #수납
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    consultation_id = models.ForeignKey(Consultation,on_delete=models.CASCADE)
    class Meta:
        db_table ="payment"
        verbose_name = "수납"
              
