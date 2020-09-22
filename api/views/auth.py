
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status

from api.serializers.auth import RegisterSerializer
from api.serializers.users import UserBasicSerializer
from rest_framework.views import APIView as RestApiView


class AuthAPIView(RestApiView):
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


class CustomkAuthToken(ObtainAuthToken, AuthAPIView):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return self.login(user)


class RegisterView(AuthAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return self.login(user)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
