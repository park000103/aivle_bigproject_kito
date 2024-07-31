from django.db import models
from datetime import date
 
class Patient(models.Model):
    patient_name = models.CharField(max_length=200, verbose_name="환자 이름")
    patient_birth = models.DateField(verbose_name="생년월일")
    patient_bday = models.CharField(max_length=6, blank=True, verbose_name="생년월일(YYMMDD)")
    patient_bday_formatted = models.CharField(max_length=20, blank=True, verbose_name="생년월일(YY년 M월 D일)")
 
    def save(self, *args, **kwargs):
        # 날짜 형식을 YYMMDD로 변환하여 저장
        if isinstance(self.patient_birth, date):
            self.patient_bday = self.patient_birth.strftime('%y%m%d')
            self.patient_bday_formatted = f"{self.patient_birth.strftime('%y년')}" \
                                          f" {self.patient_birth.month}월 {self.patient_birth.day}일"
        super(Patient, self).save(*args, **kwargs)
 
    def __str__(self):
        return self.patient_name
 
    class Meta:
        db_table = "patient"
        verbose_name = "환자"
        verbose_name_plural = "환자"