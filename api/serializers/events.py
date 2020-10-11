
from django.utils import timezone
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
                  'meeting_url', 'start_time', 'end_time', 'event_code', 'owner']


class EventListSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'name', 'summary', 'start_time', 'end_time', 'mode', 'status']

    def get_status(self, event):
        if event.end_time < timezone.now():
            return 'CLOSED'
        elif event.start_time > timezone.now():
            return 'OPEN'
        return 'PROGRESS'
