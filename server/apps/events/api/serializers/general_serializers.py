from apps.events.models import Event, Category

from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    """
    place = serializers.StringRelatedField()
    date = serializers.StringRelatedField()
    los anteriores causan probemas con las Views
    """

    def to_representation(self, instance):
        return{
            'id':instance.id,
            'name': instance.name,
            'category': instance.category.name,
            'date': instance.date,
            'place': instance.place.name if instance.place != '' else '',
        }

    class Meta:
        model = Event
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date',]

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date',]