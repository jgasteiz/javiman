from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, DeleteView, View, ListView
from google.appengine.api import users

from blog.models import Post, Photo
from cms.forms import PostForm, PhotoForm


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


class PhotoListView(RestrictedAccessMixin, ListView):
    model = Photo
    template_name = 'cms/photo_list.html'

photo_list = PhotoListView.as_view()


class NewPhotoView(RestrictedAccessMixin, CreateView):
    form_class = PhotoForm
    model = Photo
    success_url = reverse_lazy('cms:photo_list')
    template_name = 'cms/photo_form.html'

new_photo = NewPhotoView.as_view()


class UpdatePhotoView(RestrictedAccessMixin, UpdateView):
    form_class = PhotoForm
    model = Photo
    success_url = reverse_lazy('cms:photo_list')
    template_name = 'cms/photo_form.html'

update_photo = UpdatePhotoView.as_view()


class DeletePhotoView(RestrictedAccessMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('cms:photo_list')
    template_name = 'cms/photo_confirm_delete.html'

delete_photo = DeletePhotoView.as_view()


class SetPhotoOrderView(RestrictedAccessMixin, View):
    model = Photo

    def post(self, request, *args, **kwargs):
        photo = self.model.objects.get(pk=kwargs.get('pk'))
        order_modifier = int(request.POST.get('order_modifier'))
        if order_modifier > 0:
            photo.increase_order_and_save()
        else:
            photo.decrease_order_and_save()
        photo.save()
        return redirect('cms:photo_list')

set_photo_order = SetPhotoOrderView.as_view()
