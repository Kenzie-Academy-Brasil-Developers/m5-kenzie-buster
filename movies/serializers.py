from rest_framework import serializers
from .models import RatingOptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.serializers import UserSerializer


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser
        return token


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10, blank=True, default=""
    )
    rating = serializers.ChoiceField(
        max_length=20,
        choices=RatingOptions.choices,
        default=RatingOptions.G
    )
    synopsis = serializers.CharField(
        blank=True, default="")
    added_by = UserSerializer(read_only=True)
