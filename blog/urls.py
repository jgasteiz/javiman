from django.conf.urls import url, include

from rest_framework import routers

from blog.api import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    url(r'^about/$', 'blog.views.about', name='about'),
    url(r'^photos/$', 'blog.views.photos', name='photos'),

    url(r'^api/', include(router.urls)),

    url(r'^p/(?P<slug>[\w-]+)/$', 'blog.views.post', name='post'),
    url(r'^$', 'blog.views.home', name='home'),
]
