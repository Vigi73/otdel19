from django.shortcuts import render
from .models import Sert_post

# Create your views here.

def sert_list(request):
    sert_lists = Sert_post.objects.all()
    return render(request, 'sert/sert.html', {'sert_lists': sert_lists})