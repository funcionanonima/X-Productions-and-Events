from apps.events.models import Event, Category

from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    place = serializers.StringRelatedField()
    date = serializers.StringRelatedField()

    class Meta:
        model = Event
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date',]

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date',]