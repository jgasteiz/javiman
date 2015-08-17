import json

from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, TemplateView
import requests

from blog.models import Post, Photo


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


class PhotoListView(ListView):
    model = Photo
    template_name = 'blog/photos.html'

    def get_queryset(self):
        return self.model.objects.published()

photos = PhotoListView.as_view()


class AboutView(TemplateView):
    template_name = 'blog/about.html'

about = AboutView.as_view()
