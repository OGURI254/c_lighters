from django.contrib import admin
from .models import Category, Service, ServiceImage, Ministry, MinistryImage

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