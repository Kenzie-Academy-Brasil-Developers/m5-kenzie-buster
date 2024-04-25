from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsUserOwnerAuthenticated
from django.shortcuts import get_object_or_404
from users.models import User
from users.serializers import UserSerializer

# Create your views here.
class UserView(APIView):
 authentication_classes = [JWTAuthentication]
 permission_classes = [IsUserOwnerAuthenticated]
 
 def post(self, request: Request) -> Response:
  serializer = UserSerializer(data=request.data)

  serializer.is_valid(raise_exception=True)
  serializer.save()

  return Response(serializer.data, status=status.HTTP_201_CREATED)
 
 def get(self, request, user_id):
   user = get_object_or_404(User, id=user_id) 

   self.check_object_permissions(request, user)

   serializer = UserSerializer(user)

   return Response(serializer.data, status.HTTP_200_OK)
 
 def patch(self, request, user_id):
   user = get_object_or_404(User, id=user_id) 

   self.check_object_permissions(request, user)
   serializer = UserSerializer(user, data=request.data, partial=True)

   serializer.is_valid(raise_exception=True)
   serializer.save()

   return Response(serializer.data, status.HTTP_200_OK)