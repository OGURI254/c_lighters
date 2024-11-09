# api/admin.py
from django.contrib import admin
from .models import Event,EventRegistration
from django.contrib.admin.widgets import AdminTimeWidget
from django.forms import ModelForm, TimeInput
from import_export import resources
from import_export.admin import ExportMixin

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'time': AdminTimeWidget(),  # Use AdminTimeWidget for the time field
        }

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventForm
    list_display = ['name', 'date', 'time', 'venue', 'is_active', 'image']
    fields = ('name', 'description', 'date', 'time', 'venue', 'image')
    list_filter = ['is_active', 'date']
    search_fields = ['name', 'venue']


# Define a resource for EventRegistration
class EventRegistrationResource(resources.ModelResource):
    class Meta:
        model = EventRegistration
        fields = ('id', 'name', 'phone_number', 'email', 'event__name', 'registered_at')
        export_order = ('id', 'name', 'phone_number', 'email', 'event__name', 'registered_at')

@admin.register(EventRegistration)
class EventRegistrationAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = EventRegistrationResource
    list_display = ('name', 'phone_number', 'email', 'event', 'registered_at','validated')
    search_fields = ('name', 'phone_number', 'email')
    list_filter = ('event', 'registered_at')