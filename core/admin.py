from django.contrib import admin

# Register your models here.
from core.models import Country


@admin.register(Country)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'is_worldwide')
    list_filter = ('is_active', 'is_worldwide')