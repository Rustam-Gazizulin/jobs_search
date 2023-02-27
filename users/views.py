from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserCreateSerializer


class UserCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserLogOut(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
