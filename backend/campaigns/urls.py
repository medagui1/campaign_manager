from django.urls import path
from .views import CampaignListAPIView, CampaignDetailAPIView, SubscribeToCampaignAPIView

urlpatterns = [
    path("", CampaignListAPIView.as_view(), name='campaigns'),
    path("<str:slug>/", CampaignDetailAPIView.as_view(), name='campain_detail'),
]