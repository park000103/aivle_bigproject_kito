from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_date', 'patient_id', 'doctor_id', 'reservation_status')
    search_fields = ('patient_id__patient_name', 'doctor_id__doctor_name')
    list_filter = ('reservation_status', 'doctor_id', 'reservation_date')
    ordering = ('reservation_date',)
    
    fieldsets = (
        (None, {
            'fields': ('reservation_date', 'patient_id', 'doctor_id', 'reservation_status')
        }),
    )