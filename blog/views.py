from django.views.generic.list import ListView

from blog.models import Post


class HomeView(ListView):
    model = Post
    template_name = 'home.html'

home = HomeView.as_view()
