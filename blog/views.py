from django.shortcuts import render

from .models import Post


def blogs(request):
    posts = Post.objects.all()
    return render(request, 'blog/blogs.html', {'posts': posts})
