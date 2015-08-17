from django.test import TestCase

from .models import Photo


class PhotoTestCase(TestCase):
    def setUp(self):
        self.photo = Photo(
            title='Stained Glass',
            subtitle='Canterbury Cathedral',
            is_published=True,
            url='https://farm1.staticflickr.com/431/19871282374_102b88bb01_b.jpg'
        )

    def test_get_flickr_preview(self):
        preview_url = 'https://farm1.staticflickr.com/431/19871282374_102b88bb01_m.jpg'
        self.assertEqual(self.photo.get_flickr_preview(), preview_url)
