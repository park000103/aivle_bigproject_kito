from django.urls import path
from .views import PaymentCreateAPIView,PaymentListAPIView
from . import views

urlpatterns = [
    path('create/', PaymentCreateAPIView.as_view(), name='payment-create'),#수납테이블 추가
    path('list/', PaymentListAPIView.as_view(), name='payment-list'),
    path('list/<int:patient_id>/', PaymentListAPIView.as_view(), name='payment-list'),
]