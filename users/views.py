from django.shortcuts import render
from rest_framework.views import Response, Request, status, APIView

from users.serializers import LoginSerializer, UserSerializer
from users.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


# class LoginView(TokenObtainPairView):
#     ...


# class LoginViewOld_2(APIView):
#     def post(self, request: Request) -> Response:
#         serializer = TokenObtainPairSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         return Response(serializer.validated_data, status.HTTP_200_OK)


# class LoginViewOld_1(APIView):
#     def post(self, request: Request) -> Response:
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = authenticate(**serializer.validated_data)

#         if not user:
#             return Response(
#                 {
#                     "detail": "No active account found with the given credentials"
#                 },
#                 status.HTTP_401_UNAUTHORIZED,
#             )

#         refresh = RefreshToken.for_user(user)

#         token_dict = {
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#         }

#         return Response(token_dict, status.HTTP_200_OK)
