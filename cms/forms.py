from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'slug', 'body', 'is_published', 'created')
        model = Post
