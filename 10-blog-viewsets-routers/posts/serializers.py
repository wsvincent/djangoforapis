from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at",
        )


class UserSerializer(serializers.ModelSerializer):  # new

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
        )
