from django.shortcuts import render
from .models import Phone

# Create your views here.

def phone_list(request):
    phones = Phone.objects.all()
    return render(request, 'phone/phone.html', {'phones': phones})