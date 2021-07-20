from django.contrib import admin
from django.urls import path

from apps.cities.api.views.general_views import CityListAPIView

urlpatterns = [
    path('cities/', CityListAPIView.as_view(), name = 'ciudades'),
]