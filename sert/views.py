from django.shortcuts import render

from django.core.paginator import Paginator
from .models import Sert_post
# Create your views here.

def sert_list(request):
    posts = Sert_post.objects.all()

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
        'page_object1': page,
        'is_paginated1': is_paginated,
        'next_url1': next_url,
        'prev_url1': prev_url

    }

    return render(request, 'sert/sert.html', context=context)