from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from rest_framework.pagination import PageNumberPagination
from movies.models import Movie
from movies.permissions import IsMovieOwner, IsSuperOrReadOnly
from users.models import User
from movies.serializers import MovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperOrReadOnly, IsMovieOwner]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        if request.user.is_employee:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {
                    "detail": "You do not have \
permission to perform this action."
                },
                status=status.HTTP_403_FORBIDDEN,
            )


class MovieDetailView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperOrReadOnly, IsMovieOwner]

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, pk=movie_id)

        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, pk=movie_id)
        self.check_object_permissions(request, movie)

        if request.user.is_employee:
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {
                    "detail": "You do not have \
permission to perform this action."
                },
                status=status.HTTP_403_FORBIDDEN,
            )
