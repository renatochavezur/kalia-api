
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView as rest_APIView
from rest_framework.permissions import IsAuthenticated


class APIView(rest_APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_user(self):
        return self.request.user

    def get_student(self):
        if hasattr(self.request.user, 'student'):
            return self.request.user.student
        return None

    def get_teacher(self):
        if hasattr(self.request.user, 'teacher'):
            return self.request.user.teacher
        return None
