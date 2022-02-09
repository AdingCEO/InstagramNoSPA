from django.urls import path, re_path
from django.contrib.auth.validators import UnicodeUsernameValidator
from . import views

app_name = 'instagram'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('<str:username>/', views.user_page, name='user_page'),
]