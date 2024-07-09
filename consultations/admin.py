from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'doctor_id', 'consultation_date', 'amount', 'reservation_id')
    search_fields = ('patient_id__name', 'doctor_id__name', 'reservation_id__id')
    list_filter = ('consultation_date', 'doctor_id')

@admin.register(DetailConsultation)
class DetailConsultationAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'consultation_id')
    search_fields = ('name', 'consultation_id__id')
    list_filter = ('consultation_id__consultation_date',)