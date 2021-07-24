from rest_framework.response import Response
from rest_framework import generics, status

from apps.base.api import GeneralListApiView
from apps.events.api.serializers.general_serializers import CategorySerializer, EventSerializerFormated, EventSerializer


class CategoryListAPIView(GeneralListApiView):
    serializer_class = CategorySerializer


class EventListAPIView(GeneralListApiView):
    serializer_class = EventSerializer


class EventListFormatedAPIView(GeneralListApiView):
    serializer_class = EventSerializerFormated


class EventCreateAPIView(generics.CreateAPIView):
    serializer_class = EventSerializerFormated

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Evento creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = EventSerializerFormated

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)


class EventDestroyAPIView(generics.DestroyAPIView):
    serializer_class = EventSerializerFormated

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    # softDelete, si no se aclara borra diretamente
    def delete(self, request, pk=None):
        event = self.get_queryset().filter(id=pk).first()
        if event:
            event.state = False
            event.save()
            return Response({'message': 'Evento Borrada correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'No existe Evento con estos datos'}, status=status.HTTP_400_BAD_REQUEST)


class EventUpdateAPIView(generics.UpdateAPIView):
    serializer_class = EventSerializerFormated

    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(state=True).filter(id=pk).first()

    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            event_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(event_serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'No existe Evento con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            event_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if event_serializer.is_valid():
                event_serializer.save()
                return Response(event_serializer.data, status=status.HTTP_200_OK)
            return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
