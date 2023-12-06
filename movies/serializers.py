from rest_framework import serializers
from .models import RatingOptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.serializers import UserSerializer
from .models import Movie
from users.models import User


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
        max_length=10, allow_blank=True, default=""
    )
    rating = serializers.ChoiceField(
        choices=RatingOptions.choices,
        default=RatingOptions.G
    )
    synopsis = serializers.CharField(
        max_length=999,
        allow_blank=True,
        default="")
    added_by = serializers.EmailField(max_length=20, source="email", read_only=True)

    def create(self, validated_data):
        user_id = validated_data.get(user)

        email = User.objects.get(id=user_id)
        print(email)
        movie = Movie.objects.create(**validated_data,
                                     user=user_id)
        print(movie, ".............................")

        return movie
