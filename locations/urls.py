from django.urls import path

from locations.views import LocationsListView

urlpatterns = [
    # seeker view urls
    path('', LocationsListView.as_view(), name='locations_list'),
]
