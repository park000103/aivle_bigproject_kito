from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'patient_birth', 'patient_bday','patient_bday_formatted')
    search_fields = ('patient_name',)
    list_filter = ('patient_birth',)

    fieldsets = (
        (None, {
            'fields': ('patient_name', 'patient_birth', 'patient_bday','patient_bday_formatted')
        }),
    )
