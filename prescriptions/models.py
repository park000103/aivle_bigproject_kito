from django.db import models
from consultations.models import Consultation
from doctors.models import Doctor
from patients.models import Patient
# Create your models here.
class Prescription(models.Model): #처방
    consultation_id = models.ForeignKey(Consultation,on_delete=models.CASCADE, verbose_name="진료")
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE, verbose_name="환자", blank=True, null=True)
    doctor_id =models.ForeignKey(Doctor,on_delete=models.CASCADE,verbose_name="의사", blank=True, null=True)
    prescription_image = models.ImageField(upload_to='images/prescriptions',verbose_name="처방전")
    def save(self, *args, **kwargs):
        if self.consultation_id:
            self.patient_id = self.consultation_id.patient_id
            self.doctor_id = self.consultation_id.doctor_id
        super(Prescription, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient_id} - {self.doctor_id}"
    class Meta:
        db_table = "prescription"
        verbose_name = "처방"
        verbose_name_plural = "처방"