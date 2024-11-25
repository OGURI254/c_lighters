from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<slug:slug>/', views.service_details, name='service_details'),
    path('blogs/', views.blog, name='blog'),
    path('blogs/<slug:slug>/', views.blog_details, name='blog_details'),
    path('sermons/', views.sermons, name='sermons'),
    path('sermons/<slug:slug>/', views.sermon_details, name='sermon_details'),
    path('cell-groups/', views.cell_groups, name='campaign'),
    path('ministries/', views.ministries, name='ministries'),
    path('ministries/<slug:slug>/', views.ministry_details, name='ministry_details'),
    path('pastors/', views.pastor, name='pastor'),
    path('galleries/', views.gallery, name='gallery'),
    path('contacts/', views.contact, name='contact'),
    path('validate/', views.scanner, name='validate'),
    path('validate/<str:tkt_no>', views.validate_tkt, name='validate_tkt'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('events/', views.event, name='events'),
    path('ways-to-give/', views.ways_to_give, name='ways_to_give'),
    path('events/<slug:slug>/', views.event_details, name='event_details')
]
