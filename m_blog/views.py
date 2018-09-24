from django.shortcuts import render, get_object_or_404
from .models import *


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'm_blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'm_blog/post_detai.html', {'post': post})
