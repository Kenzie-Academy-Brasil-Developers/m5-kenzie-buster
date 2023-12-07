from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status, Response, Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
)

from .serializers import UserSerializer

from rest_framework.pagination import PageNumberPagination
from users.models import User
from kenzie_buster.permissions import IsUser


class UserView(APIView, PageNumberPagination):

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated, IsUser)

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        update_user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, update_user)

        existing_user = request.data
        serializer = UserSerializer(update_user, data=existing_user, partial=True)

        serializer.is_valid()

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
