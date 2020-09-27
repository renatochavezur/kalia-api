
from rest_framework import serializers

from app.events.models import Event


class EventBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'summary', 'place']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'owner', 'summary', 'description', 'mode', 'place', 'maps_url', 
                  'meeting_url', 'start_time', 'end_time', 'event_code']
