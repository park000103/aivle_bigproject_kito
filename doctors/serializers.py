from rest_framework import serializers
from .models import Doctor
from reservations.models import Reservation


class DoctorSerializer(serializers.ModelSerializer):
    reservations_count = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'doctor_name', 'departments_id', 'information', 'reservations_count']

    def get_reservations_count(self, doctor):
        reservations_count = Reservation.objects.filter(doctor_id=doctor.id, reservation_status__in=[0, 1, 2]).count()
        return reservations_count