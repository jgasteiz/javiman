from django.conf.urls import url


urlpatterns = [
    url(r'^new_post/$', 'cms.views.new_post', name='new_post'),
    url(r'^$', 'cms.views.post_list', name='post_list'),
]
