from django.contrib.auth import get_user_model
from rest_framework import viewsets  # new

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):  # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
