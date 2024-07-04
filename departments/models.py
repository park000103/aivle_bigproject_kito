from django.db import models
# Create your models here.
class FloorMap(models.Model): #층지도
    floor = models.IntegerField()
    floor_image = models.ImageField()
    class Meta:
        db_table = "floor_map"
        verbose_name = "층지도"

class Disease(models.Model): #질병
    disease_name = models.CharField(max_length=200)
    class Meta:
        db_table = "disease"
        verbose_name = "질병"
        
class Departments(models.Model): #진료부서
    departments_name = models.CharField(max_length=100)
    diseases = models.ManyToManyField(Disease)
    class Meta:
        db_table = "departments"
        verbose_name = "진료부서"


class DepartmentLocations(models.Model): #과 지도
    departments_id = models.ForeignKey(Departments,on_delete=models.CASCADE)
    departments_image = models.ImageField()
    class Meta:
        db_table = "department_locations"
        verbose_name = "과별 지도"