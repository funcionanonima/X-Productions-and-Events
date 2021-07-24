from rest_framework import serializers

from apps.members.api.serializers.general_serializers import MemberSerializerFormated
from apps.events.models import Event, Category
from apps.members.models import Member


class EventSerializerFormated(serializers.ModelSerializer):
    members = MemberSerializerFormated(many=True, read_only=True)
    place = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        events_info = validated_data.pop('members')
        member = Member.objects.create(**validated_data)
        for event_info in events_info:
            Member.objects.create(member=member, **event_info)
            return member


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date', ]
