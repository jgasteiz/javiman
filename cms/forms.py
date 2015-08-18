from django import forms
from blog.models import Post, Photo


class PostForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'slug', 'body', 'is_published', 'created',)
        model = Post


class PhotoForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'subtitle', 'url', 'is_published', 'order',)
        model = Photo
