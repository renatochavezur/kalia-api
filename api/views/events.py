
from api.serializers.events import EventBasicSerializer
from api.serializers.events import EventSerializer
from api.mixins import APIView
from app.events.models import Event

from rest_framework import generics


class EventListView(APIView, generics.ListAPIView):
    serializer_class = EventBasicSerializer
    queryset = Event.objects.all()

    def get_queryset(self):
        return self.queryset


class EventView(APIView, generics.RetrieveAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    look_up = 'id'
