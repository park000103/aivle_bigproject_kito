from rest_framework import serializers
from .models import Doctor
from reservations.models import Reservation
from departments.serializers import DepartmentsSerializer


class DoctorSerializer(serializers.ModelSerializer):
    department = DepartmentsSerializer(source='departments_id', read_only=True)
    reservations_count = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'doctor_name', 'department', 'information', 'reservations_count']

    def get_reservations_count(self, doctor):
        reservations_count = Reservation.objects.filter(doctor_id=doctor.id, reservation_status__in=[0, 1, 2]).count()
        return reservations_count