from django.conf.urls import url


urlpatterns = [
    url(r'^posts/$', 'cms.views.post_list', name='post_list'),
    url(r'^new_post/$', 'cms.views.new_post', name='new_post'),
    url(r'^update_post/(?P<pk>\d+)/$', 'cms.views.update_post', name='update_post'),
    url(r'^delete_post/(?P<pk>\d+)/$', 'cms.views.delete_post', name='delete_post'),

    url(r'^photos/$', 'cms.views.photo_list', name='photo_list'),
    url(r'^new_photo/$', 'cms.views.new_photo', name='new_photo'),
    url(r'^update_photo/(?P<pk>\d+)/$', 'cms.views.update_photo', name='update_photo'),
    url(r'^delete_photo/(?P<pk>\d+)/$', 'cms.views.delete_photo', name='delete_photo'),

    url(r'^$', 'cms.views.post_list', name='post_list'),
]
