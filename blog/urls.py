from django.conf.urls import url


urlpatterns = [
    url(r'^about/*$', 'blog.views.about', name='about'),

    url(r'^(?P<slug>[\w-]+)/*$', 'blog.views.post', name='post'),
    url(r'^$', 'blog.views.home', name='home'),
]
