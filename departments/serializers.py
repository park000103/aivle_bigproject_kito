from rest_framework import serializers
from .models import *

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['id','departments_name']

class DepartmentLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentLocations
        fields = ['departments_id', 'departments_image']

class FloorMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorMap
        fields = ['floor', 'floor_image']