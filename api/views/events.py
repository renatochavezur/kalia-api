
from rest_framework.response import Response
from rest_framework import status, viewsets

from api.mixins import APIView
from api.serializers.events import EventSerializer, UploadEventSerializer
from app.events.models import Event


class EventViewSet(APIView, viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = UploadEventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        event = Event.objects.create(
            name=data['name'],
            owner=self.get_user(),
            summary=data['summary'],
            description=data['description'],
            mode=data['mode'],
            place=data['place'],
            maps_url=data['maps_url'],
            meeting_url=data['meeting_url'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            event_code=Event.generate_event_code()
        )
        response_data = self.get_serializer(event, many=False).data
        headers = self.get_success_headers(response_data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

    def enrolled_events(self):
        user = self.get_user()
        events_id = user.enrollments.values_list('event_id', flat=True)
        queryset = self.queryset.filter(pk__in=events_id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def own_events(self):
        queryset = self.queryset.filter(owner=self.get_user())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
