from django.conf.urls import url


urlpatterns = [
    url(r'^new_post/$', 'cms.views.new_post', name='new_post'),
    url(r'^update_post/(?P<pk>\d+)/$', 'cms.views.update_post', name='update_post'),
    url(r'^delete_post/(?P<pk>\d+)/$', 'cms.views.delete_post', name='delete_post'),
    url(r'^$', 'cms.views.post_list', name='post_list'),
]
