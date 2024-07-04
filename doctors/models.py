from django.db import models
from departments.models import Departments,Disease

# Create your models here.
class Doctor(models.Model): #의사
    doctor_name = models.CharField(max_length=100)
    departments_id = models.ForeignKey(Departments,on_delete=models.CASCADE)
    information = models.TextField()
    diseases = models.ManyToManyField(Disease)
    class Meta:
        db_table = "doctor"
        verbose_name = "의사"