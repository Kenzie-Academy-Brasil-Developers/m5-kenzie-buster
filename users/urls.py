from django.urls import path
from users.views import UserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
   path('users/', UserView.as_view()),
   path('users/<int:user_id>/',UserView.as_view()),
   path('users/login/', TokenObtainPairView.as_view()),   
]