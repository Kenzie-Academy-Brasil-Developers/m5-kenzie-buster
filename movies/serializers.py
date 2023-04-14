from rest_framework import serializers
from movies.models import Movie
from .models import RatingChoices


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10, allow_null=True, default=None
        )
    rating = serializers.ChoiceField(
        RatingChoices, default=RatingChoices.G, allow_null=True
    )
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj) -> str:
        return obj.user.email

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)
