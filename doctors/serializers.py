from rest_framework import serializers
from .models import Doctor
from reservations.models import Reservation
from datetime import datetime, time

class DoctorSerializer(serializers.ModelSerializer):
    reservations_count = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'doctor_name', 'departments_id', 'information', 'reservations_count']

    def get_reservations_count(self, doctor):
        # 현재 날짜와 시간을 가져옵니다.
        now = datetime.now().date()  # 현재 날짜를 가져옵니다 (시간대 정보 없음)
        today_start = datetime.combine(now, time.min)  # 오늘 날짜의 시작 시간 (00:00:00)
        today_end = datetime.combine(now, time.max)    # 오늘 날짜의 끝 시간 (23:59:59)

        reservations_count = Reservation.objects.filter(
            doctor_id=doctor.id,
            reservation_status__in=[0, 1, 2],
            reservation_date__range=(today_start, today_end)  # 예약 날짜 필드를 기준으로 필터링
        ).count()

        return reservations_count