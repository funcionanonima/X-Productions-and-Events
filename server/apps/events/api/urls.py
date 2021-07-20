from django.contrib import admin
from django.urls import path

from apps.events.api.views.general_views import EventListAPIView, CategoryListAPIView

urlpatterns = [
    path('events/', EventListAPIView.as_view(), name = 'eventos'),
    path('categories/', CategoryListAPIView.as_view(), name = 'categorias'),
]