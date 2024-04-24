from rest_framework import serializers
from movies_orders.models import MovieOrder

class MovieOrderSerializer(serializers.Serializer):
 id = serializers.IntegerField(read_only=True)

 title = serializers.CharField(max_length=127, read_only=True, source='movie.title')
 purchased_at = serializers.DateTimeField(read_only=True)
 price = serializers.DecimalField(max_digits=8, decimal_places=2)
 purchased_by = serializers.EmailField(source='order.email', read_only=True)

 def create(self, validated_data) -> MovieOrder:
   return MovieOrder.objects.create(**validated_data)