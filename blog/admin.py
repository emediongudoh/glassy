from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'date_published', 'author']


admin.site.register(Post, PostAdmin)
