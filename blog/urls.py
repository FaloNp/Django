from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('search/', search, name='search'),
    path('sort/', sort, name='sort'),
    path('add/', add_post, name='add'),
    path('accounts/login/', user_login, name='login'),  # Użyj własnego widoku logowania
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]