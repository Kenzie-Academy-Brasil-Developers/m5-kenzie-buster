from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import User
from users.permissions import UserIsOwner

from .serializers import UserSerializer


class UsersView(APIView):
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UsersDetailsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, UserIsOwner | IsAdminUser]

    def get(self, request, user_id) -> Response:
        users = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request=request, obj=users)

        serializer = UserSerializer(users)

        return Response(serializer.data)
