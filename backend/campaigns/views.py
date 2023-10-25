from django.shortcuts import render
from rest_framework import generics
from .models import Campaign
from .serializers import CampaignSerializer, SubsciberSerializer


# Create your views here.
class CampaignListAPIView(generics.ListAPIView) :
    serializer_class = CampaignSerializer
    
    def get_queryset(self) : 
        return Campaign.objects.all()