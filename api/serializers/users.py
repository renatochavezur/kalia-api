
from rest_framework import serializers

from app.users.models import User


class UserBasicSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username']