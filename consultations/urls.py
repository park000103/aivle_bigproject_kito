from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('bfpayment/', ConsultationPaymentListView.as_view(), name='consultation-payment-list'),
    path('bfpayment/<int:patient_id>/', ConsultationPaymentListView.as_view(), name='consultation-payment-list'),#수납전 당일 진료 리스트
    path('afpayment/', ConsultationPayListView.as_view(), name='detailconsultation-list'),
    path('afpayment/<int:patient_id>/', ConsultationPayListView.as_view(), name='detailconsultation-list-filter'),
    path('afpayment/detail/<int:consultation_id>/', ConsultationPayView.as_view(), name='detailconsultation-filter'),
    path('search/', search_patient_view, name='search-patient'),
    path('search/results/', patient_search_results, name='patient-search-results'),
    path('search/results/page', patient_search_results_page, name='patient-search-results-page'),
    path('search/consultations/', patient_consultations, name='patient-consultations'),
    path('search/consultations/page', patient_consultations_page, name='patient-consultations-page'),
    path('detail_consultations_list/', detail_consultations_list, name='detail_consultations_list'),
    path('detailconsul/page', detailconsul_page, name='detailconsul_page'),
    path('<int:consultation_id>/detail/', consultation_detail_view, name='consultation-detail'),
]