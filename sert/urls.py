from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.sert_list, name='sert_list_url'),

]