from datetime import date
from django.db import models

# Create your models here.

class Patient(models.Model):  # 환자
    patient_name = models.CharField(max_length=200)
    patient_birth = models.DateField()
    patient_bday = models.CharField(max_length=6, blank=True)  # blank=True 제거 가능


    def save(self, *args, **kwargs):
        # 날짜 형식을 YYMMDD로 변환하여 저장
        if isinstance(self.patient_birth, date):
            self.patient_bday = self.patient_birth.strftime('%y%m%d')
        super(Patient, self).save(*args, **kwargs)

    def __str__(self):
        return self.patient_name

    class Meta:
        db_table = "patient"
        verbose_name = "환자" # 관리자 화면에 보일 떄 한국어로
        #일단 db에 만들려면 settings에서 installed app에 추가 
        #그다음에 python manage.py makemigrations 와 migrate를 해줘야함 