from django.utils.text import slugify
from django.db import models

from markupfield.fields import MarkupField


class Post(models.Model):
    title = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    slug = models.CharField(max_length=128, blank=True)
    body = MarkupField(default_markup_type='markdown')
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
