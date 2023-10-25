from django.urls import path
from .views import CampaignListAPIView

urlpatterns = [
    path("", CampaignListAPIView.as_view(), name='campaigns')
]