from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from event.forms import EventForm
from .models import *


class EventListView(ListView):
    model = Event
    queryset = Event.objects.filter(is_active=True)


class UserEventListView(ListView):
    model = Event
    slug_field = 'user'

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs['slug'])
        if self.user == self.request.user:
            return Event.objects.filter(user=self.user)
        else:
            return Event.objects.filter(user=self.user, is_active=True)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the website
        context['specific_user'] = self.user

        return context

class CountryEventListView(ListView):
    model = Event
    slug_field = 'country'

    def get_queryset(self):
        country = get_object_or_404(Country, slug=self.kwargs['slug'])
        return Event.objects.filter(country = country, is_active=True)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        country = get_object_or_404(Country, slug=self.kwargs['slug'])
        # Add in the website
        context['specific_country'] = country
        context['country_list'] = Country.objects.filter(is_active=True).exclude(id = country.id)

        return context


class EventCreateView(CreateView):
    model = Event
    template_name = 'event/event_form.html'
    form_class = EventForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country_list'] = Country.objects.filter(is_active=True)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreateView, self).form_valid(form)


class EventDetailView(DetailView):
    model = Event

    def dispatch(self, request, *args, **kwargs):
        """ Добавляем просмотры """
        obj = self.get_object()
        obj.views = obj.views + 1
        obj.save()
        return super(EventDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        context['joined_users'] = EventParticipant.objects.filter(event=event)
        if self.request.user.is_authenticated:
            context['event_participant'] = EventParticipant.objects.filter(user=self.request.user,
                                                                       event=event).exists()

        return context


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm

    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only owners can unpublish bugs """
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect(obj)
        return super(EventUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country_list'] = Country.objects.filter(is_active=True)
        return context


class EventPublishView(UpdateView):
    model = Event
    fields = []

    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only owners can publish bugs """
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect(obj)
        return super(EventPublishView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = True
        # self.object.published_at = timezone.now()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EventUnpublishView(UpdateView):
    model = Event
    fields = []

    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only owners can unpublish bugs """
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect(obj)
        return super(EventUnpublishView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UserJoinView(UpdateView):
    model = Event
    fields = []

    def form_valid(self, form):
        ep = EventParticipant.objects.create(event=self.object, user=self.request.user)
        ep.save()

        return super(UserJoinView, self).form_valid(form)


class UserUnjoinView(UpdateView):
    model = Event
    fields = []

    def form_valid(self, form):
        ep = get_object_or_404(EventParticipant, event = self.kwargs['pk'], user = self.request.user)
        ep.delete()

        return super(UserUnjoinView, self).form_valid(form)