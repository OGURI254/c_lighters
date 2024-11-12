from datetime import datetime
import requests

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Service, Ministry, Sermon, Blog, CellGroup, Contact, Pastor, Gallery, CommonPage, Event

def home(request):
    events = Event.objects.filter(is_active=True, date__gt=datetime.now())
    context = {
        'title': 'Homepage',
        'events': events.filter(is_special=False)[:3],
        'special_event': events.filter(is_special=True).first(),
        'services': Service.objects.filter(is_active=True)[:4],
        'ministries': Ministry.objects.filter(is_active=True)[:3],
        'sermons': Sermon.objects.filter(is_active=True)[:3],
        'blogs': Blog.objects.filter(is_published=True)[:3],
    }
    return render(request, 'index.html', context)

# About Us Page
def about(request):
    context = {
        'title': 'About Us'
    }
    return render(request, 'about.html', context)

# Services Page
def services(request):
    context = {
        'title': 'Services',
        'services': Service.objects.filter(is_active=True)
    }
    return render(request, 'service.html', context)

# Service Details Page
def service_details(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    context = {
        'title': service.title,
        'service': service,
        'services': Service.objects.filter(is_active=True)
    }
    return render(request, 'service-single.html', context)

# Blog Page
def blog(request):
    paginator = Paginator(Blog.objects.filter(is_published=True), 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Blogs',
        'blogs': page_obj
    }
    return render(request, 'blog.html', context)

# Blog Details Page
def blog_details(request, slug):
    blog = get_object_or_404(Blog, slug=slug, is_published=True)
    context = {
        'title': blog.title,
        'blog': blog,
    }
    return render(request, 'blog-single.html', context)

# Sermons Page
def sermons(request):
    paginator = Paginator(Sermon.objects.filter(is_active=True), 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Sermons',
        'sermons': page_obj
    }
    return render(request, 'sermons.html', context)

# Sermon Details Page
def sermon_details(request, slug):
    sermon = get_object_or_404(Sermon, slug=slug, is_active=True)
    context = {
        'title': sermon.title,
        'sermon': sermon,
    }
    return render(request, 'sermons-single.html', context)

def cell_groups(request):
    paginator = Paginator(CellGroup.objects.filter(is_active=True), 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Cell Groups',
        'cellgroups': page_obj
    }
    return render(request, 'campaign.html', context)

# Ministries Page
def ministries(request):
    paginator = Paginator(Ministry.objects.filter(is_active=True), 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Ministries',
        'ministries': page_obj
    }
    return render(request, 'ministries.html', context)

# Ministry Details Page
def ministry_details(request, slug):
    ministry = get_object_or_404(Ministry, slug=slug, is_active=True)
    context = {
        'title': ministry.title,
        'ministry': ministry,   
    }
    return render(request, 'ministry-single.html', context)

# Pastor Page
def pastor(request):
    paginator = Paginator(Pastor.objects.filter(user__is_active=True), 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Pastors',
        'pastors': page_obj
    }
    return render(request, 'pastor.html', context)

# Gallery Page
def gallery(request):
    paginator = Paginator(Gallery.objects.filter(is_active=True), 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Gallery',
        'images': page_obj
    }
    return render(request, 'gallery.html', context)

# Contact Us Page
def contact(request):
    if request.method == 'POST':
        pass
    context = {
        'title': 'Contact Us',
    }
    return render(request, 'contact.html', context)

# @require_staff
def scanner(request):
    context = {
        'title': 'QR Code Scanner/Reader',
    }
    return render(request, 'scanner.html', context)

def terms(request):
    page = CommonPage.objects.filter(title__icontains="Terms").first()
    context = {
        'title': page.title,
        'page': page
    }
    return render(request, 'common.html', context)

def privacy(request):
    page = CommonPage.objects.filter(title__icontains="Privacy").first()
    context = {
        'title': page.title,
        'page': page
    }
    return render(request, 'common.html', context)
