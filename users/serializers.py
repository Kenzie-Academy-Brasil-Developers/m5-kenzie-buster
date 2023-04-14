from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150, validators=[UniqueValidator(queryset=User.objects.all(), message="username already taken.")])
    password = serializers.CharField(max_length=127, write_only=True)
    email = serializers.CharField(max_length=127, validators=[UniqueValidator(queryset=User.objects.all(), message="email already registered.")])
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)   
    
    def validate(self, data):
        if data["is_employee"] is True:
            data["is_superuser"] = True
        return data