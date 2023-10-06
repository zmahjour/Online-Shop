from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phone_number", "full_name"]


class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True, allow_null=False)


