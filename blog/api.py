from rest_framework import routers, serializers, viewsets

from blog.models import Post
from blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.published()
    serializer_class = PostSerializer
