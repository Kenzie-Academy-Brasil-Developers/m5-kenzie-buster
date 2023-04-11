from django.shortcuts import render
from rest_framework.views import Response, Request, status, APIView

from users.serializers import UserSerializer
from users.models import User

# Create your views here.


class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(**serializer.validated_data)
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_201_CREATED)
