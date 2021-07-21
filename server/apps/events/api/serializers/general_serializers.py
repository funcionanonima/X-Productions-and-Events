from rest_framework import serializers

from apps.events.models import Event, Category
from apps.members.api.serializers.general_serializers import MemberSerializer


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class EventFormatedSerializer(serializers.ModelSerializer):
    """
    date = serializers.StringRelatedField()
    place = serializers.StringRelatedField()
    los anteriores causan probemas con las Views

    members= MemberSerializer(many=True)
    members = serializers.StringRelatedField(many=True)
    """

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(data)
        return{
            'id': instance.id,
            'name': instance.name,
            'category': instance.category.name,
            'date': instance.date,
            'place': instance.place.name if instance.place != '' else '',
            'members': {instance.members.name}
        }

    class Meta:
        model = Event
        exclude = ['state', 'created_date',
                   'modified_date', 'deleted_date']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date', ]
