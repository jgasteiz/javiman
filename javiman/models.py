from django.db import models


class FlickrSettings(models.Model):
    api_key = models.CharField(max_length=256)
    user_id = models.CharField(max_length=256)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(FlickrSettings, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
