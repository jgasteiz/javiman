from django.conf.urls import url


urlpatterns = [
    url(r'^about/$', 'blog.views.about', name='about'),
    url(r'^albums/$', 'blog.views.album_list', name='album_list'),
    # url(r'^albums/(?P<slug>[\w-]+)/$', 'blog.views.album_detail', name='album_detail'),

    url(r'^p/(?P<slug>[\w-]+)/$', 'blog.views.post', name='post'),
    url(r'^$', 'blog.views.home', name='home'),
]
