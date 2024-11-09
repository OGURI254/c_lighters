# api/models.py
from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField(default=timezone.now)
    venue = models.CharField(max_length=255)
    custom_fields = models.JSONField(default=dict, blank=True, null=True)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)  # Optional field
    registered_at = models.DateTimeField(auto_now_add=True)
    validated = models.BooleanField(default=False)  # New field for tracking validation

    class Meta:
        unique_together = ('event', 'email')  # Ensure unique registration per email per event

    def __str__(self):
        return f"{self.name} - {self.event.name}"



class AdminSettings(models.Model):
    validation_password = models.CharField(max_length=100, default='admin')  # Default password

    def __str__(self):
        return "Admin Settings"