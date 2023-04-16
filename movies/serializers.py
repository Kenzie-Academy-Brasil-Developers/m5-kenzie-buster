from rest_framework import serializers
from movies.models import Movie, Ratings, MovieOrder

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(allow_null=True, default=None)
    rating = serializers.ChoiceField(allow_null=True, choices=Ratings.choices, default=Ratings.DEFAULT)
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.CharField(read_only=True, source="user.email")

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)
    
class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = serializers.DateTimeField(read_only=True)
    buyed_by = serializers.SerializerMethodField()

    def get_title(self, obj):
        title = obj.movie.title
        return title
    
    def get_buyed_by(self, obj):
        buyed_by = obj.user.email
        return buyed_by

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)