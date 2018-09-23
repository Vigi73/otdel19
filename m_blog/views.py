from django.shortcuts import render
from .models import *


def post_list(request):
    posts = Post.objects.all()

    return render(request, 'm_blog/post_list.html', {'posts': posts})

