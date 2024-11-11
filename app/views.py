import requests

from django.shortcuts import render
from .models import Service, Ministry, Sermon, Blog, CellGroup, Contact

def home(request):
    api_url = 'http://localhost:8000/events/'  
    try:
        response = requests.get(api_url)
        events = response.json() if response.status_code == 200 else []
    except requests.exceptions.RequestException:
        events = []
    context = {
        'title': 'Homepage',
        'events': events 
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
        'title': 'Services'
    }
    return render(request, 'service.html', context)

# Service Details Page
def service_details(request, slug):
    return render(request, 'service-single.html')

# Blog Page
def blog(request):
    context = {
        'title': 'Blogs',
    }
    return render(request, 'blog.html', context)

# Blog Details Page
def blog_details(request, slug):
    return render(request, 'blog-single.html')

# Sermons Page
def sermons(request):
    context = {
        'title': 'Sermons',
    }
    return render(request, 'sermons.html', context)

# Sermon Details Page
def sermon_details(request, slug):
    return render(request, 'sermons-single.html')

def cell_groups(request):
    context = {
        'title': 'Cell Groups',
    }
    return render(request, 'campaign.html', context)

# Ministries Page
def ministries(request):
    context = {
        'title': 'Ministries'
    }
    return render(request, 'ministries.html', context)

# Ministry Details Page
def ministry_details(request, slug):
    return render(request, 'ministry-single.html')

# Pastor Page
def pastor(request):
    context = {
        'title': 'Pastors',
    }
    return render(request, 'pastor.html', context)

# Gallery Page
def gallery(request):
    context = {
        'title': 'Gallery',
    }
    return render(request, 'gallery.html', context)

# Contact Us Page
def contact(request):
    context = {
        'title': 'Contact Us',
    }
    return render(request, 'contact.html', context)

# scanner
def scanner(request):
    context = {
        'title': 'Scanners',
    }
    return render(request, 'scanner.html', context)
