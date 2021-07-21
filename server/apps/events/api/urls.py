from django.contrib import admin
from django.urls import path

from apps.events.api.views.general_views import EventCreateAPIView, EventListAPIView, EventRetrieveAPIView, EventDestroyAPIView, EventUpdateAPIView, EventFormatedListAPIView

urlpatterns = [
    path('', EventListAPIView.as_view(), name='events'),
    path('formated/', EventFormatedListAPIView.as_view(), name='events_formated'),
    path('create/', EventCreateAPIView.as_view(), name='event_create'),
    path('<int:pk>/', EventRetrieveAPIView.as_view(), name='event_retrieve'),
    path('destroy/<int:pk>/', EventDestroyAPIView.as_view(), name='event_destroy'),
    path('update/<int:pk>/', EventUpdateAPIView.as_view(), name='event_update'),
]
