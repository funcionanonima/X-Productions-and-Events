from django.urls import path

from apps.cities.api.views.general_views import CityListAPIView, CityRetrieveAPIView, CityDestroyAPIView

urlpatterns = [
    path('', CityListAPIView.as_view(), name = 'cities'),
    path('<int:pk>/', CityRetrieveAPIView.as_view(), name = 'cities_retrieve'),
    path('destroy/<int:pk>/', CityDestroyAPIView.as_view(), name = 'cities_destroy'),
]