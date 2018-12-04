from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q


def post_list(request):

    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__contains=search_query) | Q(text__contains=search_query))

    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    context = {
            'page_object': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url,

        }

    return render(request, 'm_blog/post_list.html', context=context)



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    f = str(post.files).split('/')[-1]
    return render(request, 'm_blog/post_detai.html', {'post': post, 'file_name': f})
