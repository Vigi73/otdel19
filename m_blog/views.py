from django.shortcuts import render, get_object_or_404
from .models import Post
from django.db.models import Q

def post_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__contains=search_query) | Q(text__contains=search_query) | Q(date_create__day=str(search_query)))
    else:
        posts = Post.objects.all()

    return render(request, 'm_blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'm_blog/post_detai.html', {'post': post})
