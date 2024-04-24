from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from movies.models import Movie
from movies_orders.serializers import MovieOrderSerializer
from movies_orders.permissions import IsAuthenticated

# Create your views here.
class MovieOrderView(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]

  def post(self, request: Request, movie_id: int) -> Response:
   movie = get_object_or_404(Movie, pk=movie_id)

   serializer = MovieOrderSerializer(data=request.data)

   serializer.is_valid(raise_exception=True)
   serializer.save(order=request.user, movie=movie)

   return Response(serializer.data, status=status.HTTP_201_CREATED)
