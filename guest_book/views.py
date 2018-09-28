from django.shortcuts import render


def guest_list(request):
    return render(request, 'guest_book/guest_book.html', {})