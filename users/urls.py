from django.urls import path
from .views import UserView
from rest_framework_simplejwt import views  # new

urlpatterns = [
    path('users/',
         UserView.as_view()
         ),
]
