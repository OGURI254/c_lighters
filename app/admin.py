from django.contrib import admin
from .models import FAQ, Blog, Category, CellGroup, Contact, Gallery, Partner, Pastor, Reel, Sermon, Service, ServiceImage, Ministry, MinistryImage, CommonPage, Event, EventRegistration, EventSchedule, Schedule, EventGallery, EventFAQ, EventPartner, EventReel, EventTestimony, Testimony

# Register your models here.
class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 0

class MinistryImageInline(admin.TabularInline):
    model = MinistryImage
    extra = 0

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['activity', 'start_at', 'end_at']
    search_fields = ['activity',]
    list_filter = ['start_at', 'end_at']
    ordering = ['start_at']
    list_per_page = 20

@admin.register(FAQ)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'created_at']
    search_fields = ['question',]
    list_filter = ['created_at', 'updated_at']
    ordering = ['question']
    list_per_page = 20

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo', 'created_at']
    search_fields = ['name',]
    list_filter = ['created_at', 'updated_at']
    ordering = ['name']
    list_per_page = 20

@admin.register(Reel)
class ReelAdmin(admin.ModelAdmin):
    list_display = ['video', 'created_at', 'updated_at']
    search_fields = ['video',]
    list_filter = ['created_at', 'updated_at']
    ordering = ['video']
    list_per_page = 20

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'created_at']
    search_fields = ['name',]
    list_filter = ['created_at', 'updated_at']
    ordering = ['created_at']
    list_per_page = 20

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at', 'updated_at']
    readonly_fields = ['slug', ]
    search_fields = ['title',]
    list_filter = ['is_active', 'created_at', 'updated_at']
    date_hierarchy = 'updated_at'
    ordering = ['is_active', 'updated_at']
    list_per_page = 20

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'is_active', 'created_at', 'updated_at']
    readonly_fields = ['slug', ]
    search_fields = ['title', 'overview']
    list_filter = ['is_active', 'created_at', 'updated_at']
    date_hierarchy = 'updated_at'
    ordering = ['is_active', 'updated_at']
    list_per_page = 20
    inlines = [ServiceImageInline]

@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    list_display = ['title', 'front_img', 'is_active', 'created_at', 'updated_at']
    readonly_fields = ['slug', ]
    search_fields = ['title', 'description']
    list_filter = ['is_active', 'created_at', 'updated_at']
    date_hierarchy = 'updated_at'
    ordering = ['is_active', 'updated_at']
    list_per_page = 20
    inlines = [MinistryImageInline]

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'img', 'is_published', 'created_at', 'updated_at']
    readonly_fields = ['slug', ]
    search_fields = ['title', 'description']
    list_filter = ['is_published', 'created_at', 'updated_at']
    date_hierarchy = 'updated_at'
    ordering = ['is_published', 'updated_at']
    list_per_page = 20

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'category__title', 'start_time', 'end_time', 'is_active', 'updated_at']
    readonly_fields = ['slug', ]
    search_fields = ['title', 'name', 'description', 'category__title']
    list_filter = ['is_active', 'category', 'created_at', 'updated_at']
    date_hierarchy = 'start_time'
    ordering = ['is_active', 'start_time']
    list_per_page = 20

@admin.register(CellGroup)
class CellGroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'img', 'whatsapp_link', 'is_active', 'updated_at']
    search_fields = ['title', 'description']
    list_filter = ['is_active', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ['is_active', 'created_at']
    list_per_page = 20

@admin.register(Pastor)
class PastorAdmin(admin.ModelAdmin):
    list_display = ['user__first_name', 'user__last_name', 'position', 'user__is_active', 'updated_at']
    search_fields = ['position', 'first__name']
    list_filter = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ['created_at']
    list_per_page = 20

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['img', 'created_at', 'updated_at']
    search_fields = ['img', ]
    list_filter = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ['updated_at', 'created_at']
    list_per_page = 20

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'is_addressed', 'updated_at']
    search_fields = ['fist_name', 'email', 'phone_number', 'last_name', 'description']
    list_filter = ['is_addressed', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ['is_addressed', 'created_at']
    list_per_page = 20

@admin.register(CommonPage)
class CommonPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'updated_at', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['is_active', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ['is_active', 'created_at']
    list_per_page = 20

class EventRegistrationInline(admin.TabularInline):
    model = EventRegistration
    readonly_fields = ['name', 'phone_number', 'email', 'is_validated', 'created_at']
    extra = 0

class EventScheduleInline(admin.TabularInline):
    model = EventSchedule
    autocomplete_fields = ['event', 'schedule']
    extra = 0

class EventGalleryInline(admin.TabularInline):
    model = EventGallery
    autocomplete_fields = ['event', 'gallery']
    extra = 0

class EventFAQInline(admin.TabularInline):
    model = EventFAQ
    autocomplete_fields = ['event', 'faq']
    extra = 0

class EventPartnerInline(admin.TabularInline):
    model = EventPartner
    autocomplete_fields = ['event', 'patner']
    extra = 0

class EventReelInline(admin.TabularInline):
    model = EventReel
    autocomplete_fields = ['event', 'reel']
    extra = 0

class EventTestimonyInline(admin.TabularInline):
    model = EventTestimony
    autocomplete_fields = ['event', 'testimony']
    extra = 0

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'venue', 'date', 'img', 'is_active', 'is_special', 'updated_at']
    search_fields = ['title', 'venue', 'description']
    list_filter = ['is_active', 'is_special', 'date', 'created_at', 'updated_at']
    date_hierarchy = 'date'
    readonly_fields = ['slug', ]
    ordering = ['is_active', '-date']
    list_per_page = 20
    inlines = [EventRegistrationInline, EventScheduleInline, EventGalleryInline, EventFAQInline, EventPartnerInline, EventReelInline, EventTestimonyInline]

@admin.register(EventRegistration)
class EventRegAdmin(admin.ModelAdmin):
    list_display = ['name', 'event', 'phone_number',  'email', 'is_validated', 'updated_at']
    search_fields = ['name', 'phone_number', 'email']
    list_filter = ['is_validated', 'email', 'event', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ['is_validated', 'created_at']
    list_per_page = 20
