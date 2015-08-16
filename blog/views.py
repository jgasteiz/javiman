import json

from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, TemplateView
import requests

from blog.models import Post
from javiman.models import FlickrSettings


class HomeView(ListView):
    model = Post
    paginate_by = 3
    template_name = 'blog/home.html'

    def get_queryset(self):
        return self.model.objects.published()

home = HomeView.as_view()


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    slug_field = 'slug'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not self.object.is_published:
            return redirect(reverse('blog:home'))

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

post = PostView.as_view()


def get_flickr_photo_url(json_photo):
    base_url = 'https://farm{farm_id}.staticflickr.com/{server_id}/{id}_{secret}.jpg'
    return base_url.format(
        farm_id=json_photo.get('farm'),
        server_id=json_photo.get('server'),
        id=json_photo.get('id'),
        secret=json_photo.get('secret')
    )


def get_flickr_album_list_request_url():
    base_url = 'https://api.flickr.com/services/rest/?method=flickr.photosets.getList&api_key={api_key}&user_id={user_id}&format=json&nojsoncallback=1'
    flickr_settings = FlickrSettings.objects.get()
    return base_url.format(
        api_key=flickr_settings.api_key,
        user_id=flickr_settings.user_id,
    )


def get_flickr_album_photo_list_request_url(album_id):
    base_url = 'https://api.flickr.com/services/rest/?method=flickr.photosets.getPhotos&api_key={api_key}&photoset_id={album_id}&user_id={user_id}&per_page=3&format=json&nojsoncallback=1'
    flickr_settings = FlickrSettings.objects.get()
    return base_url.format(
        api_key=flickr_settings.api_key,
        album_id=album_id,
        user_id=flickr_settings.user_id,
    )


class AlbumListView(TemplateView):
    template_name = 'blog/photos.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(AlbumListView, self).get_context_data(*args, **kwargs)

        cached_album_list = cache.get('album_list')
        if cached_album_list is None:
            # Get the list of albums in flickr
            response = requests.get(get_flickr_album_list_request_url())
            if response.status_code == 200:
                json_response = json.loads(response.content)
                json_albums = json_response.get('photosets').get('photoset')
                album_list = [{
                    'id': album.get('id'),
                    'title': album.get('title').get('_content'),
                    'description': album.get('description').get('_content'),
                } for album in json_albums]

                # Get the first picture of the album as highlight
                for album in album_list:
                    album_photos_response = requests.get(get_flickr_album_photo_list_request_url(album.get('id')))
                    if album_photos_response.status_code == 200:
                        json_album_photos_response = json.loads(album_photos_response.content)
                        json_album_photos = json_album_photos_response.get('photoset').get('photo')
                        photos = [{
                            'title': photo.get('title'),
                            'url': get_flickr_photo_url(photo)
                        } for photo in json_album_photos]
                        album['photos'] = photos

                cache.set('album_list', album_list)
                ctx['album_list'] = album_list
            else:
                ctx['album_list'] = []
        else:
            ctx['album_list'] = cached_album_list

        return ctx

album_list = AlbumListView.as_view()


class AboutView(TemplateView):
    template_name = 'blog/about.html'

about = AboutView.as_view()
