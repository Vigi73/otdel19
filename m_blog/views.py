from django.shortcuts import render
from .models import *


def post_list(request):
    return render(request, 'm_blog/post_list.html', {})

