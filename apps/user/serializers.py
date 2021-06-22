from rest_framework import serializers
from apps.user.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id", "password"]


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id", "username", "password"]
