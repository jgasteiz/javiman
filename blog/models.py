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


class PhotoManager(models.Manager):
    def get_queryset(self):
        return super(PhotoManager, self).get_queryset()

    def published(self):
        return super(PhotoManager, self).get_queryset().filter(is_published=True)


class Photo(models.Model):
    title = models.CharField(max_length=256, blank=True)
    subtitle = models.CharField(max_length=256, blank=True)
    url = models.CharField(max_length=256)
    is_published = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = PhotoManager()

    class Meta:
        ordering = ('order', '-created',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            for photo in Photo.objects.filter(order__gte=self.order):
                photo.order += 1
                photo.save()
        super(Photo, self).save(*args, **kwargs)

    def decrease_order_and_save(self):
        self.order = max(0, self.order - 1)
        # Get the photo with the same order as this photo and increase its order.
        photo_qs = Photo.objects.filter(order=self.order)
        if photo_qs.exists():
            photo = photo_qs[0]
            photo.order = self.order + 1
            photo.save()
        self.save()

    def increase_order_and_save(self):
        self.order += 1
        # Get the photo with the same order as this photo and decrease its order.
        photo_qs = Photo.objects.filter(order=self.order)
        if photo_qs.exists():
            photo = photo_qs[0]
            photo.order = self.order - 1
            photo.save()
        self.save()

    def get_flickr_preview(self):
        """
        This will only work for jpeg images stored in flickr.
        Given a url like:
            //farm1.staticflickr.com/702/20638346971_1c14fc9bff_l.jpg,
        this will return something like:
            //farm1.staticflickr.com/702/20638346971_1c14fc9bff_m.jpg
        """
        image_url = self.url[:-6]
        return '{}_m.jpg'.format(image_url)
