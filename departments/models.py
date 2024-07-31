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

        
class Departments(models.Model): #진료부서
    departments_name = models.CharField(max_length=100,verbose_name="진료부서명")
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