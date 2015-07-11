from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created', 'updated')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
