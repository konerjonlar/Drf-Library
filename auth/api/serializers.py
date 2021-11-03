from auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")
