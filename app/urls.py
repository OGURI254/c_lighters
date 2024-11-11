# app/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('service/<slug:slug>/', views.service_details, name='service_details'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_details, name='blog_details'),
    path('sermons/', views.sermons, name='sermons'),
    path('sermons/<slug:slug>/', views.sermon_details, name='sermon_details'),
    path('cell-groups/', views.cell_groups, name='campaign'),
    path('ministries/', views.ministries, name='ministries'),
    path('ministry/<slug:slug>/', views.ministry_details, name='ministry_details'),
    path('pastor/', views.pastor, name='pastor'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('validate/', views.scanner, name='scanner'),
]
