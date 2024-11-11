from django import forms
from .models import Event

class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name','description', 'date', 'time', 'venue', 'is_active', 'custom_fields']
        widgets = {
            'custom_fields': forms.HiddenInput()
        }
