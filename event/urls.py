from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import *

app_name = 'event'
urlpatterns = [
    path('list/', EventListView.as_view(), name='list'),
    path('user/<slug>/list/', UserEventListView.as_view(), name='user-list'),
    path('country/<slug>/list/', CountryEventListView.as_view(), name='country-list'),
    path('create/', EventCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', login_required(EventUpdateView.as_view()), name='edit'),
    path('<int:pk>/', EventDetailView.as_view(), name='detail'),
    path('<int:pk>/publish/', login_required(EventPublishView.as_view()), name='publish'),
    path('<int:pk>/unpublish/', login_required(EventUnpublishView.as_view()), name='unpublish'),
    path('<int:pk>/join/', login_required(UserJoinView.as_view()), name='user-join'),
    path('<int:pk>/unjoin/', login_required(UserUnjoinView.as_view()), name='user-unjoin'),
]