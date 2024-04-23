from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsSuperuserOrReadOnly
from movies.permissions import IsMovieOwner
from django.shortcuts import get_object_or_404

# Create your views here.

class MovieView(APIView):
 authentication_classes = [JWTAuthentication]
 permission_classes = [IsSuperuserOrReadOnly]
 
 def post(self, request: Request) -> Response:
   serializer = MovieSerializer(data=request.data)

   serializer.is_valid(raise_exception=True)
   serializer.save(user=request.user)

   return Response(serializer.data, status.HTTP_201_CREATED)
 
 def get(self, request: Request) -> Response:
   movies = Movie.objects.all()

   serializer = MovieSerializer(movies, many=True)

   return Response(serializer.data, status.HTTP_200_OK)
 
class MovieDetailView(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsSuperuserOrReadOnly]

  def get(self, request: Request, movie_id: int) -> Response:
     movie = get_object_or_404(Movie, pk=movie_id)

     serializer = MovieSerializer(movie)

     return Response(serializer.data, status.HTTP_200_OK)
  
  
  def delete(self, request: Request, movie_id: int) -> Response:
    movie = get_object_or_404(Movie, pk=movie_id)

    self.check_object_permissions(request, movie)

    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
