from rest_framework.views import APIView, status, Response, Request

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
)

from .serializers import MovieOrderSerializer
from movies.models import Movie
from django.shortcuts import get_object_or_404


class MovieOrderView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, pk=movie_id)

        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        serializer.save(user=user, movie=movie)

        return Response(serializer.data, status.HTTP_201_CREATED)
