from django import forms

from event.models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'start_at', 'short_description', 'full_description', 'country', 'url', 'url_id',
                  'url_password']
