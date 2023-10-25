from django.shortcuts import render
from rest_framework import generics, response, status
from .models import Campaign, Subscriber
from .serializers import CampaignSerializer, SubscriberSerializer
from django.http import Http404


# Create your views here.
class CampaignListAPIView(generics.ListAPIView) :
    serializer_class = CampaignSerializer
    
    def get_queryset(self) : 
        return Campaign.objects.all()

class CampaignDetailAPIView(generics.RetrieveAPIView) : 
    serializer_class = CampaignSerializer
    
    def get_object(self) :
        slug = self.kwargs.get("slug")
        
        try :
            return Campaign.objects.get(slug = slug)
        except Campaign.DoesNotExist :
            raise Http404("Campaign not found")
        
class SubscribeToCampaignAPIView(generics.CreateAPIView) : 
    serializer_class = SubscriberSerializer