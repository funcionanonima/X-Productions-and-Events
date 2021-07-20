from apps.cities.models import Cities

from rest_framework import serializers

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Cities
        exclude = ['state']
