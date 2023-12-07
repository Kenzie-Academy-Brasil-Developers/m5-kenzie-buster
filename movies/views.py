from rest_framework.views import APIView, status, Response, Request

from .serializers import MovieSerializer
from .models import Movie

from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import MyCustomPermission


# class LoginJWTView(TokenObtainPairView):
#     serializer_class = CustomJWTSerializer


class MovieView(APIView, PageNumberPagination):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (MyCustomPermission,)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user_id = request.user.id
        serializer.save(user_id=user_id)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        print(movies)
        return Response(MovieSerializer(movies, many=True).data, status.HTTP_200_OK)


class MovieDetailView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (MyCustomPermission,)

    def get(self, request: Request, movie_id: int) -> Response:

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
            remove_movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"detail": error_message},
                status.HTTP_404_NOT_FOUND
            )

        remove_movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
