
from rest_framework import serializers

from app.events.models import Event


class UploadEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'summary', 'description', 'mode', 'place', 'maps_url',
                  'meeting_url', 'start_time', 'end_time']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'summary', 'description', 'mode', 'place', 'maps_url',
                  'meeting_url', 'start_time', 'end_time', 'event_code']


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'summary', 'start_time', 'end_time', 'mode']
