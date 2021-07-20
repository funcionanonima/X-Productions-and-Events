from apps.base.api import GeneralListApiView
from apps.events.api.serializers.general_serializers import CategorySerializer, EventSerializer

class CategoryListAPIView(GeneralListApiView):
    serializer_class = CategorySerializer

class EventListAPIView(GeneralListApiView):
    serializer_class = EventSerializer