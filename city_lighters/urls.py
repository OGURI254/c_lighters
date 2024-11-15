
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('clc/', admin.site.urls),
    path('', include('app.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'City Lighters'
admin.site.site_title = 'City Lighters'
admin.site.index_title = "Admin"

