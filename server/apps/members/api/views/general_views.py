from rest_framework import generics, status
from rest_framework.response import Response

from apps.members.models import Member
from apps.members.api.serializers.general_serializers import MemberSerializer


class MemberListAPIView(generics.ListCreateAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        return Member.objects.filter(state=True)

class MemberCreateAPIView(generics.CreateAPIView):
    serializer_class = MemberSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Miembro creado correctamente'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class MemberRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

class MemberDestroyAPIView(generics.DestroyAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    #softDelete, si no se aclara borra diretamente
    def delete(self, request, pk=None):
        member = self.get_queryset().filter(id=pk).first()
        if member:
            member.state = False
            member.save()
            return Response({'message':'Miembro Borrada correctamente'}, status = status.HTTP_201_CREATED)
        return Response({'message':'No existe Miembro con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

class MemberUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(state=True).filter(id = pk).first()

    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            member_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(member_serializer.data, status = status.HTTP_201_CREATED)
        return Response({'error':'No existe Miembro con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            member_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if member_serializer.is_valid():
                member_serializer.save()
                return Response(member_serializer.data, status=status.HTTP_200_OK)
            return Response(member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)