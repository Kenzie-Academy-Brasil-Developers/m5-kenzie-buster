from rest_framework.views import APIView, status, Response, Request

from users.models import User
from .serializers import UserSerializer

from rest_framework.pagination import PageNumberPagination


class UserView(APIView, PageNumberPagination):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        # user = User.objects.create(**serializer.validated_data)
        serializer.save()

        # serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    # def get(self, request: Request) -> Response:
    #     by_trait = request.query_params.get("trait", None)
    #     if by_trait:
    #         pets = User.objects.filter(traits__name__icontains=by_trait)
    #     else:
    #         pets = User.objects.all()
    #     result = self.paginate_queryset(pets, request)
    #     serializer = UserSerializer(result, many=True)
    #     return self.get_paginated_response(serializer.data)
