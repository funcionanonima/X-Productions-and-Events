from rest_framework import generics

from apps.cities.models import Cities
from apps.cities.api.serializers.general_serializers import CitySerializer

class CityListAPIView(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        return Cities.objects.filter(state=True)
