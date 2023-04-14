from rest_framework.views import APIView, Request, Response, status
from users.models import User
from users.serializers import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status.HTTP_200_OK)

    def handle_exception(self, exc):
        if isinstance(exc, AuthenticationFailed):
            return Response(
                {
                    "detail": "No active account \
found with the given credentials"
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return super().handle_exception(exc)


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
