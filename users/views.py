from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status

from .models import User
from users.serializers import UserSerializer


class UserView(APIView):
    @staticmethod
    def get(request: Request) -> Response:
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    @staticmethod
    def post(request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
