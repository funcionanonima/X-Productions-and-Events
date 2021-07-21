from rest_framework import serializers

from apps.events.models import Event, Category
from apps.members.api.serializers.general_serializers import MemberSerializer


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date', ]
