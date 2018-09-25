from django.shortcuts import render

# Create your views here.

def blanks_list(request):
    return render(request, 'blanks/blanks.html', {})