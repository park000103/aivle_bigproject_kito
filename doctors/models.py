from django.db import models
from departments.models import Departments

# Create your models here.
class Doctor(models.Model): #의사
    doctor_name = models.CharField(max_length=100,verbose_name = "의사이름")
    departments_id = models.ForeignKey(Departments,on_delete=models.CASCADE,verbose_name = "진료부서명")
    information = models.TextField(verbose_name = "의사설명")
    class Meta:
        db_table = "doctor"
        verbose_name = "의사"
        verbose_name_plural = "의사들"
    def __str__(self):
        return self.doctor_name