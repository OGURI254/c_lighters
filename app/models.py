from django.db import models
from django.urls import reverse
from django.utils.text import Truncator
from django_ckeditor_5.fields import CKEditor5Field
from city_lighters.utils import slugify_and_append_uuid

class CommonPage(models.Model):
    title = models.CharField(max_length=120, unique=True)
    description = CKEditor5Field('Text', config_name='extends')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('is_active', 'created_at')
        verbose_name_plural = 'Common Pages'

class Category(models.Model):
    title =  models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_and_append_uuid(self.title)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('is_active', 'created_at')
        verbose_name_plural = 'Categories'

class Service(models.Model):
    title =  models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    overview = models.TextField(max_length=300)
    icon = models.ImageField(upload_to="services/icon/")
    description = CKEditor5Field('Text', config_name='default')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_and_append_uuid(self.title)
        super(Service, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('service_details', kwargs={'slug':self.slug})
    
    class Meta:
        ordering = ('is_active', 'created_at')

class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to="services/images/")

    def __str__(self):
        return self.img.name

class Ministry(models.Model):
    title =  models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    front_img = models.ImageField(upload_to="ministry/")
    description = CKEditor5Field('Text', config_name='default')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_and_append_uuid(self.title)
        super(Ministry, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('ministry_details', kwargs={'slug':self.slug})
    
    class Meta:
        ordering = ('is_active', 'created_at')
        verbose_name_plural = 'Ministries'

class MinistryImage(models.Model):
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to="ministry/images/")

    def __str__(self):
        return self.img.name

class Blog(models.Model):
    title =  models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    img = models.ImageField(upload_to="blog/")
    description = CKEditor5Field('Text', config_name='default')
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_and_append_uuid(self.title)
        super(Blog, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog_details', kwargs={'slug':self.slug})
    
    class Meta:
        ordering = ('is_published', 'created_at')

class Sermon(models.Model):
    title =  models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=120)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sermons')
    img = models.ImageField(upload_to="blog/")
    description = CKEditor5Field('Text', config_name='default')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_and_append_uuid(self.title)
        super(Sermon, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('sermon_details', kwargs={'slug':self.slug})
    
    class Meta:
        ordering = ('is_active', 'created_at')

class CellGroup(models.Model):
    title =  models.CharField(max_length=220, unique=True)
    whatsapp_link  = models.URLField()
    img = models.ImageField(upload_to="blog/")
    description = CKEditor5Field('Text', config_name='default')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('is_active', 'created_at')
        verbose_name_plural = 'Cell Groups'

class Pastor(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='user')
    position = models.CharField(max_length=120)
    img = models.ImageField(upload_to="pastor/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
    
    class Meta:
        ordering = ('position', 'created_at')

class Gallery(models.Model):
    img = models.ImageField(upload_to="gallery/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.img.name
    
    class Meta:
        ordering = ('updated_at', 'created_at')
        verbose_name_plural = 'Galleries'

class Reel(models.Model):
    video = models.FileField(upload_to="reels/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.video.name
    
    class Meta:
        ordering = ('updated_at', 'created_at')

class Contact(models.Model):
    first_name =  models.CharField(max_length=60)
    last_name =  models.CharField(max_length=60)
    email =  models.EmailField(max_length=255)
    phone_number =  models.CharField(max_length=13)
    description = models.TextField(null=True, blank=True)
    is_addressed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    
    class Meta:
        ordering = ('is_addressed', 'created_at')

import requests

class Event(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=120)
    date = models.DateTimeField()
    venue = models.CharField(max_length=120)
    theme = models.CharField(max_length=120)
    overview = models.TextField(max_length=300)
    map = models.URLField(max_length=550)
    description = CKEditor5Field('Text', config_name='default')
    is_special = models.BooleanField(default=False)
    img = models.ImageField(upload_to='events/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event_details', kwargs={'slug':self.slug})
    
    def get_overview(self):
        return Truncator(self.overview).chars(60)
    
    def get_map_url(self): 
        response = requests.head(self.map, allow_redirects=True) 
        return response.url
    
    def get_embed_url(google_maps_url): 
        api_key = ""
        embed_url = f"https://www.google.com/maps/embed/v1/place?key={api_key}&q={google_maps_url}" 
        return embed_url

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_and_append_uuid(self.title)
        if 'maps.app.goo.gl' in self.map: 
            self.map = self.get_map_url()
        super(Event, self).save(*args, **kwargs)

    class Meta:
        ordering = ('is_active', 'created_at')

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    is_validated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('event', 'email')
        verbose_name_plural = 'Event Registrations'

    def __str__(self):
        return f"{self.name} - {self.event.title}"
    
    def get_id(self):
        return str(self.id).zfill(7)
    
class Schedule(models.Model):
    activity = models.CharField(max_length=120)
    start_at = models.TimeField()
    end_at = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.start_at}-{self.end_at} - {self.activity}"
    
    class Meta:
        ordering = ['-start_at']

class EventSchedule(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="schedules")
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="schedules")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.schedule.start_at}-{self.schedule.end_at} - {self.schedule.activity}"
    
class EventGallery(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="galleries")
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name="galleries")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.gallery.img.name
    
    class Meta:
        ordering = ('is_active', 'event', 'gallery')
        verbose_name_plural = 'Event Galleries'
    
class EventReel(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="reels")
    reel = models.ForeignKey(Reel, on_delete=models.CASCADE, related_name="reels")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.reel.video.name
    
    class Meta:
        ordering = ('is_active', 'event', 'reel')
        verbose_name_plural = 'Event Reels'

class Artist(models.Model):
    first_name =  models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    about = models.TextField(max_length=450)
    image = models.ImageField(upload_to='artists/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SocialLink(models.Model):
    fb_url = models.URLField(max_length=220, unique=True, null=True, blank=True)
    ig_url = models.URLField(max_length=220, unique=True, null=True, blank=True)
    linkedin_url = models.URLField(max_length=220, unique=True, null=True, blank=True)
    x_url = models.URLField(max_length=220, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserSocialLink(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='social_links')
    link = models.ForeignKey(SocialLink, on_delete=models.CASCADE, related_name='social_links')

    def __str__(self):
        return f"{self.user.first_name} - {self.user.last_name} Social Link"

class ArtistSocialLink(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='social_links')
    link = models.ForeignKey(SocialLink, on_delete=models.CASCADE, related_name='social_link')

    def __str__(self):
        return f"{self.artist.first_name} - {self.artist.last_name} Social Link"

class Testimony(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='testimonies/')
    message = models.TextField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} Testimony"
    
class EventTestimony(models.Model):
    testimony = models.ForeignKey(Testimony, models.CASCADE, related_name="testimonies")
    event = models.ForeignKey(Event, models.CASCADE, related_name="testimonies")

    def __str__(self):
        return f"{self.event.title} Testimony"

class Partner(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to="partners/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class EventPartner(models.Model):
    patner = models.ForeignKey(Partner, models.CASCADE, related_name="partners")
    event = models.ForeignKey(Event, models.CASCADE, related_name="partners")

    def __str__(self):
        return f"{self.event.title} - {self.patner.name}"
    
class FAQ(models.Model):
    question = models.CharField(max_length=120)
    answer = models.TextField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    
class EventFAQ(models.Model):
    faq = models.ForeignKey(FAQ, models.CASCADE, related_name="faqs")
    event = models.ForeignKey(Event, models.CASCADE, related_name="faqs")

    def __str__(self):
        return f"{self.event.title} - {self.faq.question}"