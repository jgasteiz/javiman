from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'created', 'updated', 'slug', 'body')
