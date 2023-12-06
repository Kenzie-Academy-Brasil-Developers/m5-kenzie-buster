from rest_framework.views import APIView, status, Response, Request

from .serializers import UserSerializer

from rest_framework.pagination import PageNumberPagination


class UserView(APIView, PageNumberPagination):

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
