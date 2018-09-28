from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post_guest



def guest_list(request):





    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('guest_list_url')
    else:

        posts = Post_guest.objects.all()
        form = PostForm()
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
            'form': form

        }

        return render(request, 'guest_book/guest_book.html', context=context)


