from apps.members.models import Member

from rest_framework import serializers

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        exclude = ['state']