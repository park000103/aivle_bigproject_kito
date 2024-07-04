from django.db import models
from consultations.models import Consultation
from doctors.models import Doctor
from patients.models import Patient
# Create your models here.
class Prescription(models.Model): #처방
    consultation_id = models.ForeignKey(Consultation,on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor_id =models.ForeignKey(Doctor,on_delete=models.CASCADE)
    prescription_image = models.ImageField()
    class Meta:
        db_table = "prescription"
        verbose_name = "처방"