from django.views.generic import DetailView, ListView, TemplateView

from blog.models import Post


class HomeView(ListView):
    model = Post
    paginate_by = 3
    template_name = 'blog/home.html'

home = HomeView.as_view()


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    slug_field = 'slug'

post = PostView.as_view()


class AboutView(TemplateView):
    template_name = 'blog/about.html'

about = AboutView.as_view()