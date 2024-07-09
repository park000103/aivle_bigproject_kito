from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Departments)
# admin.site.register(Disease)
# admin.site.register(FloorMap)
# admin.site.register(DepartmentLocations)


@admin.register(FloorMap)
class FloorMapAdmin(admin.ModelAdmin):
    list_display = ('floor', 'floor_image')
    search_fields = ('floor',)

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('disease_name',)
    search_fields = ('disease_name',)

@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('departments_name',)
    search_fields = ('departments_name',)
    filter_horizontal = ('diseases',)

@admin.register(DepartmentLocations)
class DepartmentLocationsAdmin(admin.ModelAdmin):
    list_display = ('departments_id', 'departments_image')
    search_fields = ('departments_id__departments_name',)