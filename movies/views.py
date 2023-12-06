from rest_framework.views import APIView, status, Response, Request

from users.models import User
from .serializers import MovieSerializer

from rest_framework.pagination import PageNumberPagination
from .serializers import CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import MyCustomPermission


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


class MovieView(APIView, PageNumberPagination):

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        # user = User.objects.create(**serializer.validated_data)
        serializer.save()

        # serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_201_CREATED)
