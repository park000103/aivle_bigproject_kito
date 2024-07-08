from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'patient_id', 'payment_date', 'amount', 'payment_method', 'consultation_id']