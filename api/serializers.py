# api/serializers.py
from rest_framework import serializers
from .models import Event, EventRegistration

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventRegistrationSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())

    class Meta:
        model = EventRegistration
        fields = ['id', 'event', 'name', 'phone_number', 'email', 'registered_at', 'validated']

