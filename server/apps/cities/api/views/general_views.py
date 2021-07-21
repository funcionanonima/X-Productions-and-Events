from rest_framework import generics, status
from rest_framework.response import Response

from apps.cities.models import Cities
from apps.cities.api.serializers.general_serializers import CitySerializer

class CityListAPIView(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        return Cities.objects.filter(state=True)

class CityRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class=CitySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

class CityDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    #softDelete, si no se aclara borra diretamente
    def delete(self, request, pk=None):
        city = self.get_queryset().filter(id=pk).first()
        if city:
            city.state = False
            city.save()
            return Response({'message':'Ciudad Borrada correctamente'}, status = status.HTTP_201_CREATED)
        return Response({'message':'No existe Ciudad con estos datos'}, status = status.HTTP_400_BAD_REQUEST)