from rest_framework.views import APIView, status, Response, Request

from .permissions import MyCustomPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import MovieOrderSerializer


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def post(self, request: Request) -> Response:
        serializer = MovieOrderSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        print(request, "REQUEST")
        print(request.data, "REQUEST DATA")

        user_id = request.user.id
        serializer.save(user_id=user_id)

        return Response(serializer.data, status.HTTP_201_CREATED)
