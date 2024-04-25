from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.Serializer):
 id = serializers.IntegerField(read_only=True)

 title = serializers.CharField(max_length=127)
 duration = serializers.CharField(max_length=10, required=False)
 rating = serializers.ChoiceField(choices=Movie.rating_choices, default='G')
 synopsis = serializers.CharField(max_length=255, default='', allow_null=True)

 added_by = serializers.EmailField(source='user.email', read_only=True)

 def create(self, validated_data) -> Movie:
    return Movie.objects.create(**validated_data)
 