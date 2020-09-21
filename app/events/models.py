from django.db import models

from app.users.models import User
from app.utils.events import generate_event_code


class Event(models.Model):
    MODE_VIRTUAL = 'VIRTUAL'
    MODE_PRESENTIAL = 'PRESENTIAL'
    CODE_SIZE = 9

    MODE_CHOICES = [
        (MODE_VIRTUAL, 'virtual'),
        (MODE_PRESENTIAL, 'presential')
    ]

    name = models.CharField(max_length=64, null=True, blank=True)
    owner = models.ForeignKey(User,
                              null=True,
                              related_name='events',
                              on_delete=models.SET_NULL)
    deleted = models.BooleanField(default=True)
    summary = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    mode = models.CharField(max_length=20, choices=MODE_CHOICES, blank=True)
    place = models.CharField(max_length=128, blank=True, null=True)
    maps_url = models.CharField(max_length=256, blank=True, null=True)
    meeting_url = models.CharField(max_length=256, blank=True, null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    event_code = models.CharField(max_length=CODE_SIZE,
                                  unique=True,
                                  default=generate_event_code)

    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    modified = models.DateTimeField(auto_now=True, editable=False, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ['start_time']


class Enrollment(models.Model):
    event = models.ForeignKey(Event,
                              related_name='enrollments',
                              on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             related_name='enrollments',
                             on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.event, self.user)
