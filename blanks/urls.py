from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.blanks_list, name='blanks_list_url'),

]