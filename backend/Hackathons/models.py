# path: backend/Hackathons/models.py

from django.db import models

from Users.models import Users


class HackathonDetails(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    background_image = models.CharField(max_length=250)
    hackathon_image = models.CharField(max_length=250)
    submission_type = models.CharField(choices=[('image', 'Image'), ('file', 'File'), ('link', 'Link')], max_length=10) 
    reward_prize = models.DecimalField(max_digits=10, decimal_places=2)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 


class HackathonSubmissions(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(HackathonDetails, on_delete=models.CASCADE)
    submission_name = models.CharField(max_length=255)
    summary = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.submission_name
