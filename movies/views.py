from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Movie
from .permissions import IsEmployeeOrReadOnly
from .serializers import MovieSerializer


class CreateListMovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]

    def post(self, req: Request):
        serializer = MovieSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=req.user)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        movies = Movie.objects.all()

        pagination_movies = self.paginate_queryset(movies, req)

        serializer = MovieSerializer(pagination_movies, many=True)

        return self.get_paginated_response(serializer.data)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]

    def get(self, req: Request, movie_id: int) -> Response:
        try:
            movie = Movie.objects.get(id=movie_id)
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status.HTTP_200_OK)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, req: Request, movie_id: int) -> Response:
        try:
            movie = Movie.objects.get(id=movie_id)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
