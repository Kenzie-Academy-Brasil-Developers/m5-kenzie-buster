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
 

 def create(self, validate_date: dict) -> User:
  is_employer = validate_date.get('is_employer', False)
  validate_date['is_superuser'] = is_employer

  return User.objects.create_user(**validate_date)