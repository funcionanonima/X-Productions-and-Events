from rest_framework import generics

class GeneralListApiView(generics.ListAPIView):
    serializer_name=None

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)