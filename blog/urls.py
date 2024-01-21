from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', views.category_list, name='post_category'),
    path('search/', search, name='search'),
    path('sort/', sort, name='sort'),
    path('add/', add_post, name='add'),
    path('accounts/login/', user_login, name='login'),  # Użyj własnego widoku logowania
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]