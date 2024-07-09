from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('consultation_id', 'patient_id', 'doctor_id', 'prescription_image')
    search_fields = ('patient_id__patient_name', 'doctor_id__doctor_name')
    list_filter = ('consultation_id', 'doctor_id')

    fieldsets = (
        (None, {
            'fields': ('consultation_id', 'prescription_image')
        }),
    )
