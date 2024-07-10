from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('bfpayment/', ConsultationPaymentListView.as_view(), name='consultation-payment-list'),
    path('bfpayment/<int:patient_id>/', ConsultationPaymentListView.as_view(), name='consultation-payment-list'),#수납전 당일 진료 리스트
    path('afpayment/', ConsultationPayListView.as_view(), name='detailconsultation-list'),
    path('afpayment/<int:patient_id>/', ConsultationPayListView.as_view(), name='detailconsultation-list-filter')
]