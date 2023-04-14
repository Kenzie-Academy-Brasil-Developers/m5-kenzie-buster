from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ]
    )
    email = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="email already registered."
            )
        ]
    )

    birthdate = serializers.DateField(allow_null=True, default=None)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    is_employee = serializers.BooleanField(default=False, allow_null=True)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict) -> User:
        if validated_data["is_employee"] is True:
            validated_data["is_superuser"] = True

        return User.objects.create_user(**validated_data)
