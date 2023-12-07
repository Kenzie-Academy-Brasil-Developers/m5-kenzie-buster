from rest_framework import serializers
from .models import RatingOptions
from .models import Movie


#
# class CustomJWTSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token["is_superuser"] = user.is_superuser
#         return token
#

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
    added_by = serializers.CharField(max_length=20, source="user.email", read_only=True)

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)

        return movie
