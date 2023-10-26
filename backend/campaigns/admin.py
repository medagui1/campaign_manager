from django.contrib import admin
from .models import Campaign, Subscriber

class CampaignModelAdmin(admin.ModelAdmin) :
    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title","description")

# Register your models here.
admin.site.register(Campaign, CampaignModelAdmin)
admin.site.register(Subscriber)