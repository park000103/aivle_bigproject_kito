from django.db import models
# Create your models here.
class FloorMap(models.Model): #층지도
    floor = models.IntegerField(verbose_name="층")
    floor_image = models.ImageField(upload_to='images/floormap/',verbose_name="층 이미지")
    class Meta:
        db_table = "floor_map"
        verbose_name = "층지도"
        verbose_name_plural = "층지도"
    
    def __str__(self):
        return f"{self.floor}층"

class Disease(models.Model): #질병
    disease_name = models.CharField(max_length=200,verbose_name="질병명")
    class Meta:
        db_table = "disease"
        verbose_name = "질병"
        verbose_name_plural = "질병들"
    def __str__(self):
        return self.disease_name

        
class Departments(models.Model): #진료부서
    departments_name = models.CharField(max_length=100,verbose_name="진료부서명")
    diseases = models.ManyToManyField(Disease,blank=True, verbose_name='질병')
    class Meta:
        db_table = "departments"
        verbose_name = "진료부서"
        verbose_name_plural = "진료부서들"
    def __str__(self):
        return self.departments_name


class DepartmentLocations(models.Model): #과 지도
    departments_id = models.ForeignKey(Departments,on_delete=models.CASCADE,verbose_name="진료부서")
    departments_image = models.ImageField(upload_to='images/department/',verbose_name="진료부서 이미지")
    class Meta:
        db_table = "department_locations"
        verbose_name = "과별 지도"
        verbose_name_plural = "과별 지도들"
    def __str__(self):
        return f"{self.departments_id.departments_name} 위치"