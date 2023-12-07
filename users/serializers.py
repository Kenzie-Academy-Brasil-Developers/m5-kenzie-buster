from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(queryset=User.objects.all(),
                            message="email already registered.")
        ])
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(validators=[
        UniqueValidator(queryset=User.objects.all(),
                        message="username already taken.")
    ])
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(required=False, allow_null=True)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict):
        if validated_data["is_employee"] is False:
            user = User.objects.create_user(**validated_data)
        else:
            user = User.objects.create_superuser(**validated_data)
        return user

    def update(self, instance: User, validate_data: dict):
        for key, value in validate_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance

