# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventRegistrationViewSet, AdminSettingsViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'eventRegistration', EventRegistrationViewSet, basename='eventRegistration')
router.register(r'adminsettings', AdminSettingsViewSet, basename='adminsettings')

urlpatterns = [
    path('', include(router.urls)),
    path('eventRegistration/<int:pk>/validate_ticket/', 
         EventRegistrationViewSet.as_view({'post': 'validate_ticket'}), 
         name='validate_ticket'),
]
