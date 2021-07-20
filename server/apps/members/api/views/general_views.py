from rest_framework import generics

from apps.members.models import Member
from apps.members.api.serializers.general_serializers import MemberSerializer

class MemberListAPIView(generics.ListCreateAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        return Member.objects.filter(state=True)