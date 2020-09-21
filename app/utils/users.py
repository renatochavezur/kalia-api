
from secrets import choice

from django.apps import apps


def generate_identification_code():
    User = apps.get_model('users', 'User')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    identification_code = ''.join(choice(alphabet) for _ in range(User.IDENTIFICATION_CODE_SIZE))
    while User.objects.filter(identification_code=identification_code).exists():
        identification_code = ''.join(choice(alphabet) for _ in range(User.IDENTIFICATION_CODE_SIZE))
    return identification_code
