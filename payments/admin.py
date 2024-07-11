from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'payment_date', 'amount', 'payment_method', 'consultation_id')
    search_fields = ('patient_id__patient_name', 'payment_method')
    list_filter = ('payment_date', 'payment_method')
    fieldsets = (
        (None, {
            'fields': ('patient_id', 'amount', 'payment_method', 'consultation_id')  # 'payment_date' 제거
        }),
    )
    readonly_fields = ('payment_date',)  # 'payment_date' 필드를 읽기 전용으로 설정