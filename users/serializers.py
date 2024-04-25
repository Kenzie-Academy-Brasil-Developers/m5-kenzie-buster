from rest_framework import serializers
from users.models import User
from .utils import validate_unique_email, validate_unique_username

class UserSerializer(serializers.Serializer):
 id = serializers.IntegerField(read_only=True)

 username = serializers.CharField(max_length=150)
 password = serializers.CharField(max_length=150, write_only=True)

 email = serializers.CharField(max_length=127)
 first_name = serializers.CharField(max_length=50)
 last_name =  serializers.CharField(max_length=50)
 birthdate = serializers.DateField( default=None)
 is_employer = serializers.BooleanField(default=False)

 is_superuser = serializers.BooleanField(read_only=True)

 def validate_email(self, value):
  if validate_unique_email(value):
   raise serializers.ValidationError('email already registered.')
  return value
 
 def validate_username(self, value):
  if validate_unique_username(value):
   raise serializers.ValidationError('username already taken.')
  return value
 

 def create(self, validated_data: dict) -> User:
  is_employer = validated_data.get('is_employer', False)
  validated_data['is_superuser'] = is_employer

  return User.objects.create_user(**validated_data)
 
 def update(self, instance: User, validated_data: dict):
   instance.email = validated_data.get("email", instance.email)
   instance.first_name = validated_data.get("firts_name", instance.first_name)
   instance.last_name = validated_data.get("last_name", instance.last_name)
   instance.birthdate = validated_data.get("birthdate", instance.birthdate)

   is_employer = serializers.BooleanField(default=False)
   is_superuser = serializers.BooleanField(read_only=True)

   instance.save()

   return instance