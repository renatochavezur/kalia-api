
from secrets import choice

from django.apps import apps


IDENTIFICATION_CODE_LENGTH = 9


def generate_identification_code():
    User = apps.get_model('users', 'User')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    identification_code = ''.join(choice(alphabet) for _ in range(IDENTIFICATION_CODE_LENGTH))
    while User.objects.filter(identification_code=identification_code).exists():
        identification_code = ''.join(choice(alphabet) for _ in range(IDENTIFICATION_CODE_LENGTH))
    return identification_code
