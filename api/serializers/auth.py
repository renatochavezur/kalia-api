
from django.db import transaction
from rest_framework import serializers

from app.users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['fullname', 'phone', 'username', 'password']
        extra_kwargs = {
            'fullname': {'required': True},
            'phone': {'required': True},
            'username': {'required': True},
            'password': {'required': True}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.email = user.username
        user.set_password(validated_data.get('password'))
        with transaction.atomic():
            user.save()
        return user
