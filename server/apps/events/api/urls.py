from django.contrib import admin
from django.urls import path

from apps.events.api.views.general_views import EventCreateAPIView, EventListAPIView, EventRetrieveAPIView, EventDestroyAPIView, EventUpdateAPIView, EventListFormatedAPIView, EventRetrieveFormatedAPIView

urlpatterns = [
    path('formated/', EventListFormatedAPIView.as_view(), name='events_formated'),
    path('formated/<int:pk>', EventRetrieveFormatedAPIView.as_view(),
         name='event_formated'),
    path('', EventListAPIView.as_view(), name='events'),
    path('create/', EventCreateAPIView.as_view(), name='event_create'),
    path('<int:pk>/', EventRetrieveAPIView.as_view(), name='event_retrieve'),
    path('destroy/<int:pk>/', EventDestroyAPIView.as_view(), name='event_destroy'),
    path('update/<int:pk>/', EventUpdateAPIView.as_view(), name='event_update'),
]
