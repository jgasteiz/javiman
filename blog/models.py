import datetime
from django.utils.text import slugify
from django.db import models

from markupfield.fields import MarkupField


class PostManager(models.Manager):
    def get_queryset(self):
        return super(PostManager, self).get_queryset()

    def published(self):
        return super(PostManager, self).get_queryset().filter(is_published=True)


class Post(models.Model):
    title = models.CharField(max_length=128)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)
    slug = models.CharField(max_length=128, blank=True)
    body = MarkupField(default_markup_type='markdown')
    is_published = models.BooleanField(default=False)
    objects = PostManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.id and not self.created:
            self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created',)
