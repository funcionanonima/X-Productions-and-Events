from apps.events.models import Event, Category

from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        exclude = ['state',]

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ['state',]