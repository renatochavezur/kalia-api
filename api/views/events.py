
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status, viewsets

from api.mixins import APIView
from api.serializers.events import EventSerializer, UploadEventSerializer, EventListSerializer
from app.events.models import Event


class EventViewSet(APIView, viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

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

    def list(self, request, *args, **kwargs):
        event_code = request.query_params.get('code', None)
        term = request.query_params.get('term', None)
        owned = request.query_params.get('owned', None)
        enrolled = request.query_params.get('enrolled', None)
        event_status = request.query_params.get('status', None)
        queryset = self.get_queryset()
        user = self.get_user()
        if event_code:
            queryset = queryset.filter(event_code=event_code)
        elif term:
            queryset = queryset.filter(name__icontains=term)
        if owned:
            queryset = queryset.filter(owner=user)
        elif enrolled:
            events_id = user.enrollments.values_list('event_id', flat=True)
            queryset = queryset.filter(pk__in=events_id)
        if event_status:
            now = timezone.now()
            if event_status == 'OPEN':
                queryset = queryset.filter(start_time__gt=now)
            elif event_status == 'CLOSED':
                queryset = queryset.filter(end_time__lt=now)
            elif event_status == 'PROGRESS':
                queryset = queryset.filter(end_time__gt=now,
                                           start_time__lt=now)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = EventListSerializer(queryset, many=True)
        return Response(serializer.data)
