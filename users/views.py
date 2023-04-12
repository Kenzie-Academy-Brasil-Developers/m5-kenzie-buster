from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status

from models import User


class UserView(APIView):
    @staticmethod
    def post(request: Request):
        user = User.objects.create_user()
