from django.contrib import admin
from .models import Blog, Category, CellGroup, Contact, Gallery, Pastor, Sermon, Service, ServiceImage, Ministry, MinistryImage

# Register your models here.
class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 0

class MinistryImageInline(admin.TabularInline):
    model = MinistryImage
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'created_at', 'updated_at']
    search_fields = ['title',]
    list_filter = ['is_active', 'created_at', 'updated_at']
    date_hierarchy = 'updated_at'
    ordering = ['is_active', 'updated_at']
    list_per_page = 20

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'is_active', 'created_at', 'updated_at']
    search_fields = ['title', 'overview']
    list_filter = ['is_active', 'created_at', 'updated_at']
    date_hierarchy = 'updated_at'
    ordering = ['is_active', 'updated_at']
    list_per_page = 20
    inlines = [ServiceImageInline]

@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    list_display = ['title', 'front_img', 'is_active', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    list_filter = ['is_active', 'created_at', 'updated_at']
    date_hierarchy = 'updated_at'
    ordering = ['is_active', 'updated_at']
    list_per_page = 20
    inlines = [MinistryImageInline]

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'img', 'is_published', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    list_filter = ['is_published', 'created_at', 'updated_at']
    date_hierarchy = 'updated_at'
    ordering = ['is_published', 'updated_at']
    list_per_page = 20

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category__title', 'start_time', 'end_time', 'is_active', 'updated_at']
    search_fields = ['title', 'description', 'category__title']
    list_filter = ['is_active', 'author', 'category', 'created_at', 'updated_at']
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
    list_display = ['img', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ['is_active', 'created_at']
    list_per_page = 20

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'is_addressed', 'updated_at']
    search_fields = ['fist_name', 'email', 'phone_number', 'last_name', 'description']
    list_filter = ['is_addressed', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ['is_addressed', 'created_at']
    list_per_page = 20