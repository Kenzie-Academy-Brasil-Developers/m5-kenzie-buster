from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import UsersDetailsView, UsersView

urlpatterns = [
    path("users/", UsersView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/<int:user_id>/", UsersDetailsView.as_view()),
]
