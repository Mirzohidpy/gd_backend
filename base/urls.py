from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ServiceListView, ServiceDetailView, PartnerListView, PartnerDetailView

urlpatterns = [
    # Organization
    path('service/', ServiceListView.as_view()),
    path('service/<int:pk>/', ServiceDetailView.as_view()),
    path('partner/', PartnerListView.as_view()),
    path('partner/<int:pk>/', PartnerDetailView.as_view()),
]
