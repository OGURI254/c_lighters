import base64
from datetime import datetime
from io import BytesIO
import json
from city_lighters.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
import qrcode
from app.form import EventRegForm
from .models import EventRegistration, Service, Ministry, Sermon, Blog, CellGroup, Contact, Pastor, Gallery, CommonPage, Event

def home(request):
    events = Event.objects.filter(is_active=True, date__gte=datetime.now())
    context = {
        'title': 'Homepage',
        'events': events[:3],
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

def event_details(request, slug):
    event = get_object_or_404(Event, is_active=True, date__gte=datetime.now(), slug=slug)
    if request.method == 'POST':
        form = EventRegForm(request.POST, event=event)
        try:
            if form.is_valid():
                reg = form.save()
                send_ticket(reg.id)
                messages.success(request, f"You've successfully registered for {event.title}!")
                return redirect('home')
        except Exception as e:
            messages.warning(request, f"{e}")   
            return redirect('event_details', slug)
    else:
        form = EventRegForm(event=event) 

    context = {
        'title': event.title,
        'event': event,
        'form': form
    }
    return render(request, 'event.html', context)

def send_ticket(id):
    reg = get_object_or_404(EventRegistration, event__is_active=True, event__date__gte=datetime.now(), id=id, event__is_special=True)
    data = {
        "tkt_no": reg.get_id(),
        "name": reg.name,
        "phone_number": reg.phone_number,
        "email": reg.email,
        "event": reg.event.title,
        "is_validated": reg.is_validated
    }
    json_data = json.dumps(data)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(json_data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    context = {
        'title': reg.event.title,
        'reg': reg,
        'qr_code': img_base64,
    }
    html_body = render_to_string('ticket.html', context)
    msg = EmailMultiAlternatives(subject="Your Ticket Booking", from_email=DEFAULT_FROM_EMAIL, to=[reg.email, "o.jeff3.a@gmail.com"], body=html_body)
    msg.attach_alternative(html_body, "text/html")
    msg.send()
    