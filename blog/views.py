import json

from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, TemplateView
from django.views.decorators.cache import (
    cache_page,
    patch_cache_control,
)
from djangae.utils import on_production

from blog.models import Post, Photo

MAX_AGE = 1 if not on_production() else 90


class CacheMixin(object):
    @method_decorator(cache_page(MAX_AGE))
    def get(self, request, *args, **kwargs):
        response = super(CacheMixin, self).get(request, *args, **kwargs)
        patch_cache_control(response, public=True, max_age=MAX_AGE)
        response['Pragma'] = 'Public'
        return response


class HomeView(CacheMixin, ListView):
    model = Post
    paginate_by = 3
    template_name = 'blog/home.html'

    def get_queryset(self):
        return self.model.objects.published()

home = HomeView.as_view()


class PostView(CacheMixin, DetailView):
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


class PhotoListView(CacheMixin, ListView):
    model = Photo
    paginate_by = 12
    template_name = 'blog/photos.html'

    def get_queryset(self):
        return self.model.objects.published()

photos = PhotoListView.as_view()


class AboutView(CacheMixin, TemplateView):
    template_name = 'blog/about.html'

about = AboutView.as_view()
