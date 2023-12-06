from rest_framework.views import APIView, status, Response, Request

from .serializers import MovieSerializer
from .models import Movie

from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import AllowAny
# from .permissions import MyCustomPermission
from rest_framework.permissions import IsAuthenticated


# class LoginJWTView(TokenObtainPairView):
#     serializer_class = CustomJWTSerializer


class MovieView(APIView, PageNumberPagination):
    authentication_classes = (JWTAuthentication,)

    def post(self, request: Request) -> Response:
        permission_classes = (IsAuthenticated,)
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user_id = request.user.id
        serializer.save(user_id=user_id)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self):
        permission_classes = (AllowAny,)

        movies = Movie.objects.all()
        return Response(MovieSerializer(movies, many=True).data, status.HTTP_200_OK)


class MovieDetailView(APIView):
    def get(self, movie_id: int) -> Response:
        error_message = "Not found."
        try:
            found_movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"detail": error_message},
                status.HTTP_404_NOT_FOUND
            )

        serializer = MovieSerializer(found_movie)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        error_message = "Not found."
        try:
            remove_pet = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"detail": error_message},
                status.HTTP_404_NOT_FOUND
            )

        remove_pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
