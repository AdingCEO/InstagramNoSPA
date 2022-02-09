from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.profile_edit, name='profile_edit'),
    path('<str:username>/follow/', views.user_follow, name='user_follow'),
    path('<str:username>/unfollow/', views.user_unfollow, name='user_unfollow'),
]