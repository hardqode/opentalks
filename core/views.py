from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from core.models import Country
from event.models import Event


class IndexView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events_list'] = Event.objects.filter(is_active=True)
        context['country_list'] = Country.objects.filter(is_active=True)
        return context