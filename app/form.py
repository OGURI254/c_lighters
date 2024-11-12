from django import forms
from .models import EventRegistration
from django.core.exceptions import ValidationError

class EventRegForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['name', 'phone_number', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your name'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your phone number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your email address'
            }),
        }
    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event', None)
        super(EventRegForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        if email and self.event:
            if EventRegistration.objects.filter(email=email, event=self.event).exists():
                raise ValidationError("You are already registered for this event with this email.")

        return cleaned_data

    def save(self, commit=True):
        instance = super(EventRegForm, self).save(commit=False)
        if self.event:
            instance.event = self.event
        if commit:
            instance.save()
        return instance

        