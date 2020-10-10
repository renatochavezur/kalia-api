
from django.db import transaction
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from api.serializers.auth import RegisterSerializer
from api.serializers.users import UserBasicSerializer
from app.users.models import User
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import action


class AuthAPIViewSet(viewsets.GenericViewSet):
    def login(self, user):
        try:
            token = Token.objects.get(user=user)
            response_status = status.HTTP_200_OK
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)
            response_status = status.HTTP_201_CREATED
        response = {
            'token': token.key,
            'user': UserBasicSerializer(user).data
        }
        return Response(response, status=response_status)

    @action(methods=['post'], detail=False)
    def request_token(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return self.login(user)

    @action(methods=['post'], detail=False)
    def register(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            user = User(**validated_data)
            user.email = user.username
            user.identification_code = User.generate_identification_code()
            user.set_password(validated_data['password'])
            with transaction.atomic():
                user.save()
            return self.login(user)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
