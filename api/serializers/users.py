
from rest_framework import serializers

from app.users.models import User


class UploadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['fullname', 'phone', 'email', 'birth_day', 'dni', 'occupation',
                  'show_birth_day', 'show_dni', 'show_email', 'show_occupation', 'show_phone']


class UserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullname', 'username', 'phone', 'email', 'birth_day', 'dni', 'occupation',
                  'show_birth_day', 'show_dni', 'show_email', 'show_occupation', 'show_phone',
                  'identification_code', 'premium']
