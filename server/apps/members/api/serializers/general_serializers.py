from rest_framework import serializers

from apps.members.models import Member


class MemberSerializerFormated(serializers.ModelSerializer):
    """
    1ra Forma: Setea la lista de objetos relacionados 
    born_place = CitySerializer()
    """

    """ 
    2da Forma: Embebe el atributo __str__ de la clase
    born_place = serializers.StringRelatedField()
    """
    # 3ra Forma: Sobreescribir el metodo, se puede validar

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'name': instance.name,
            'last_name': instance.last_name,
            'identification': instance.identification,
            'born_place': instance.born_place.name if instance.born_place != '' else '',
            'company': instance.company,
        }

    class Meta:
        model = Member
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date', ]
