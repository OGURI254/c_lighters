from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import Event, EventRegistration, AdminSettings
from .serializers import EventSerializer, EventRegistrationSerializer
from io import BytesIO
import qrcode
import base64
from weasyprint import HTML

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return Event.objects.filter(is_active=True)

class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [AllowAny]
    def create(self, request, *args, **kwargs):
        event_id = request.data.get('event')
        email = request.data.get('email')
        if EventRegistration.objects.filter(event_id=event_id, email=email).exists():
            return Response(
                {"message": "You have already registered for this event."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            registration = serializer.save()
            ticket_number = f"TICKET-{registration.id:06d}"
            qr_data = f"registration_id:{registration.id}"
            qr = qrcode.make(qr_data)
            qr_buffer = BytesIO()
            qr.save(qr_buffer, format="PNG")
            qr_buffer.seek(0)
            qr_base64 = base64.b64encode(qr_buffer.getvalue()).decode("utf-8")
            logo_url = request.build_absolute_uri(settings.STATIC_URL + "/static/images/logo.png")
            context = {
                "event_name": registration.event.name,
                "event_date": registration.event.date,
                "ticket_number": ticket_number,
                "name": registration.name,
                "email": registration.email,
                "qr_code_base64": qr_base64,
                "logo_url": logo_url,
            }
            html_string = render_to_string("ticket.html", context)
            pdf_buffer = BytesIO()
            HTML(string=html_string).write_pdf(pdf_buffer)
            pdf_buffer.seek(0)
            email_message = EmailMessage(
                subject="Event Registration Confirmation",
                body="You have successfully booked a slot. Check your email to download your ticket.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[registration.email],
            )
            email_message.attach(f"ticket_{registration.id}.pdf", pdf_buffer.getvalue(), 'application/pdf')
            email_message.send()
            return Response(
                {
                    "message": "You have successfully booked a slot. Check your email to download your ticket.",
                    "registration": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], permission_classes=[AllowAny])
    def validate_ticket(self, request, pk=None):
        try:
            registration_id = request.data.get("registration_id")
            input_password = request.data.get("password")
            registration = EventRegistration.objects.get(pk=registration_id)
            admin_settings = AdminSettings.objects.first()
            if not admin_settings:
                admin_settings = AdminSettings.objects.create()
            if input_password == admin_settings.validation_password:
                registration.validated = True
                registration.save()
                return Response({"message": "Ticket validated successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid password."}, status=status.HTTP_403_FORBIDDEN)
        except EventRegistration.DoesNotExist:
            return Response({"message": "Registration not found."}, status=status.HTTP_404_NOT_FOUND)

class AdminSettingsViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]
    @action(detail=False, methods=['post'], permission_classes=[IsAdminUser])
    def set_validation_password(self, request):
        new_password = request.data.get("password")
        if new_password:
            admin_settings, created = AdminSettings.objects.get_or_create(id=1)
            admin_settings.validation_password = new_password
            admin_settings.save()
            return Response({"message": "Password updated successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Password not provided."}, status=status.HTTP_400_BAD_REQUEST)
