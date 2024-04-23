from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.Serializer):
 id = serializers.IntegerField(read_only=True)

 title = serializers.CharField(max_length=127)
 duration = serializers.CharField(max_length=10, allow_null=True)
 rating = serializers.CharField(max_length=20, default='G')
 synopsis = serializers.CharField(max_length=255, allow_null=True)

 added_by = serializers.EmailField(source='user.email', read_only=True)

 def validate_rating(self, value):
   valid_options = ['G', 'PG', 'PG-13', 'R', 'NC-17']
   if value not in valid_options:
     raise serializers.ValidationError(
       'Invalid rating option, the valid options are: G, PG, PG-13, R e NC-17.'
     )
   return value

 def create(self, validated_data) -> Movie:
    return Movie.objects.create(**validated_data)
 