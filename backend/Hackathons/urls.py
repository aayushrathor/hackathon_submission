# path: backend/Hackathons/urls.py
from django.urls import path

from Hackathons.models import HackathonDetails


urlpatterns = [
    path('', HackathonDetails)
]
