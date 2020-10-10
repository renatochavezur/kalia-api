
from api.serializers.users import UserBasicSerializer, UploadUserSerializer
from api.mixins import APIView
from app.users.models import User

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(APIView, viewsets.ModelViewSet):
    serializer_class = UserBasicSerializer
    queryset = User.objects.all()

    @action(methods=['put'], detail=False)
    def user_data(self, request, *args, **kwargs):
        user = self.get_user()
        serializer = UploadUserSerializer(data=request.data, instance=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = self.get_serializer(user, many=False).data
        return Response(user_data)
