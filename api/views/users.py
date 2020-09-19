
from api.serializers.users import UserBasicSerializer
from api.mixins import APIView

from rest_framework import generics


class UserDataView(APIView, generics.UpdateAPIView):
    serializer_class = UserBasicSerializer

    def get_object(self):
        return self.get_user()
