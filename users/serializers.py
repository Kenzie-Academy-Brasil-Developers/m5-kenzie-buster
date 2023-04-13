from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User


class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    username = serializers.CharField(validators=[
        UniqueValidator(queryset=User.objects.all(), message="username already taken.")])
    email = serializers.EmailField(max_length=127, validators=[
                                   UniqueValidator(queryset=User.objects.all(), message="email already registered.")])
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(
        read_only=True)

    def create(self, validated_data: dict) -> User:
        print(validated_data['is_employee'])
        if validated_data['is_employee']:
            validated_data['is_superuser'] = True

        return User.objects.create_user(**validated_data)
