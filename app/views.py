# app/views.py
import requests

from django.shortcuts import render

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

def about(request):
    return render(request, 'about.html')

# About Us Page
def about(request):
    return render(request, 'about.html')

# Services Page
def services(request):
    context = {
        'title': 'Services'
    }
    return render(request, 'service.html', context)

# Service Details Page
def service_details(request):
    return render(request, 'service-single.html')

# Blog Page
def blog(request):
    return render(request, 'blog.html')

# Blog Details Page
def blog_details(request):
    return render(request, 'blog-single.html')

# Sermons Page
def sermons(request):
    return render(request, 'sermons.html')

# Sermon Details Page
def sermon_details(request):
    return render(request, 'sermons-single.html')

# Campaign (Cell Groups) Page
def campaign(request):
    return render(request, 'campaign.html')

# Campaign Details Page
def campaign_details(request):
    return render(request, 'campaign-single.html')

# Ministries Page
def ministries(request):
    return render(request, 'ministries.html')

# Ministry Details Page
def ministry_details(request):
    return render(request, 'ministry-single.html')

# Pastor Page
def pastor(request):
    return render(request, 'pastor.html')

# Gallery Page
def gallery(request):
    return render(request, 'gallery.html')

# Contact Us Page
def contact(request):
    return render(request, 'contact.html')

# Custom 404 Page
def custom_404(request):
    return render(request, '404.html', status=404)
# scanner
def scanner(request):
    return render(request, 'scanner.html')
