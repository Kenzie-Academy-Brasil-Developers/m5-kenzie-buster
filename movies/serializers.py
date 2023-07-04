from rest_framework import serializers

from .models import Movie, SizeRating


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(max_length=127)

    duration = serializers.CharField(max_length=10, allow_null=True, default=None)

    rating = serializers.ChoiceField(
        choices=SizeRating.choices, default=SizeRating.size_g
    )
    synopsis = serializers.CharField(allow_null=True, default=None)

    added_by = serializers.EmailField(source="user.email", read_only=True)

    def create(self, validated_data):
        serializers = Movie.objects.create(**validated_data)
        return serializers
