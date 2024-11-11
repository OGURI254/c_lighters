# app/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('service-single/', views.service_details, name='service_details'),
    path('blog/', views.blog, name='blog'),
    path('blog-single/', views.blog_details, name='blog_details'),
    path('sermons/', views.sermons, name='sermons'),
    path('sermons-single/', views.sermon_details, name='sermon_details'),
    path('campaign/', views.campaign, name='campaign'),
    path('campaign-single/', views.campaign_details, name='campaign_details'),
    path('ministries/', views.ministries, name='ministries'),
    path('ministry-single/', views.ministry_details, name='ministry_details'),
    path('pastor/', views.pastor, name='pastor'),
    path('gallery/', views.gallery, name='gallery'),
    path('404/', views.custom_404, name='custom_404'),
    path('contact/', views.contact, name='contact'),
     path('validate/', views.scanner, name='scanner'),
]
