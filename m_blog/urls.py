from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list_url'),
    path('post/<pk>/', views.post_detail, name='post_detail_url'),
    path('blanks/', include('blanks.urls'))

]