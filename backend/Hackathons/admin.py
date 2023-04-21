
from django.contrib import admin

from Hackathons.models import HackathonDetails, HackathonSubmissions


@admin.register(HackathonDetails)
class HackathonDetailsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'background_image', 'hackathon_image', 'reward_prize', 'submission_type')
    search_fields = ('title', 'id')


@admin.register(HackathonSubmissions)
class HackathonSubmissionsAdmin(admin.ModelAdmin):
    list_display = ('users', 'hackathon', 'submission_name', 'summary', 'image', 'file', 'link')
    search_fields = ('id',)

