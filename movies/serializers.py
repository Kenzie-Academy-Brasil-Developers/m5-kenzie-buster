from rest_framework import serializers
from movies.models import Movie, Ratings

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(allow_null=True, default=None)
    rating = serializers.ChoiceField(allow_null=True, choices=Ratings.choices, default=Ratings.DEFAULT)
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.CharField(read_only=True, source="user.email")

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)