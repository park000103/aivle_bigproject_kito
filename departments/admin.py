from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Departments)
admin.site.register(Disease)
admin.site.register(FloorMap)
admin.site.register(DepartmentLocations)