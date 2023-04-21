# path: backend/Users/models.py

from django.db import models

# from Hackathons.models import HackathonDetails


class Users(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=80, blank=True, null=True, default=None) 
    phone = models.CharField(max_length=80, null=False, unique=True)
    # hackathons = models.ManyToManyField(HackathonDetails)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
