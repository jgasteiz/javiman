from django.utils.text import slugify
from django.db import models

from markupfield.fields import MarkupField


class Post(models.Model):
    title = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    slug = models.SlugField(max_length=128, blank=True)
    body = MarkupField()
    is_published = models.BooleanField(default=False)
