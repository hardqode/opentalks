from django.contrib import admin

# Register your models here.
from event.models import Event, EventParticipant


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'is_active', 'start_at')
    list_filter = ('is_active',)


@admin.register(EventParticipant)
class EventParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'event', 'created_at')