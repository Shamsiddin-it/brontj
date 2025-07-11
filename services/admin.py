from django.contrib import admin
from .models import Service, ServiceImage

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'provider', 'category', 'price', 'is_active')
    list_filter = ('is_active', 'category')
    inlines = [ServiceImageInline]

admin.site.register(ServiceImage)
