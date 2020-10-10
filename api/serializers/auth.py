
from rest_framework import serializers

from app.users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['fullname', 'username', 'password']
