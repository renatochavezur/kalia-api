
from secrets import choice

from django.apps import apps


def generate_event_code():
    Event = apps.get_model('events', 'Event')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    event_code = ''.join(choice(alphabet) for _ in range(Event.CODE_SIZE))
    while Event.objects.filter(event_code=event_code).exists():
        event_code = ''.join(choice(alphabet) for _ in range(Event.CODE_SIZE))
    return event_code
