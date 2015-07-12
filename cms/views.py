from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect
from google.appengine.api import users
from django.views.generic import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView

from blog.models import Post
from cms.forms import PostForm


class RestrictedAccessMixin(object):
    def dispatch(self, *args, **kwargs):
        if not users.is_current_user_admin():
            login_url = '{}?next={}'.format(
                reverse('login:djangae_login_redirect'),
                reverse('cms:post_list')
            )
            return redirect(login_url)
        return super(RestrictedAccessMixin, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        ctx = super(RestrictedAccessMixin, self).get_context_data(*args, **kwargs)
        ctx['user_email'] = users.get_current_user()
        return ctx


class PostListView(RestrictedAccessMixin, ListView):
    model = Post
    template_name = 'cms/post_list.html'

post_list = PostListView.as_view()


class NewPostView(RestrictedAccessMixin, CreateView):
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('cms:post_list')
    template_name = 'cms/post_form.html'

new_post = NewPostView.as_view()


class UpdatePostView(RestrictedAccessMixin, UpdateView):
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('cms:post_list')
    template_name = 'cms/post_form.html'

update_post = UpdatePostView.as_view()


class DeletePostView(RestrictedAccessMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('cms:post_list')
    template_name = 'cms/post_confirm_delete.html'

delete_post = DeletePostView.as_view()