from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('bfpayment/', ConsultationPaymentListView.as_view(), name='consultation-payment-list'), # bf는 진료 이후 수납 안된 건을 조회 -> 당일
    path('bfpayment/<int:patient_id>/', ConsultationPaymentListView.as_view(), name='consultation-payment-list'),#수납전 당일 진료 리스트
    path('afpayment/', ConsultationPayListView.as_view(), name='detailconsultation-list'),  # af는 수납테이블에서 일자 별로 조회 - 세부내역
    path('afpayment/<int:patient_id>/', ConsultationPayListView.as_view(), name='detailconsultation-list-filter'),
    path('afpayment/detail/<int:consultation_id>/', ConsultationPayView.as_view(), name='detailconsultation-filter'), # 특정 진료의 세부 내역 조회
    path('choice/', choice, name='choice'), # 세부, 납입 선택 page
    path('search/', search_patient_view, name='search-patient'), # 환자 조회 page
    path('search/results/', patient_search_results, name='patient-search-results'),
    path('search/results/page', patient_search_results_page, name='patient-search-results-page'), # 환자 목록 page
    path('search/consultations/', patient_consultations, name='patient-consultations'),
    path('search/consultations/page', patient_consultations_page, name='patient-consultations-page'), # 진료 조회 page
    path('detail_consultations_list/', detail_consultations_list, name='detail_consultations_list'),
    path('detailconsul/page', detailconsul_page, name='detailconsul_page'),
    path('<int:consultation_id>/detail/', consultation_detail_view, name='consultation-detail'),
]