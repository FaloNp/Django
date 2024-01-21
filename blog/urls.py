from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #path('add/', add_post, name='add_post'),
    path('accounts/login/', user_login, name='login'),  # Użyj własnego widoku logowania
    path('accounts/', include('django.contrib.auth.urls')),
    #path('login/', user_login, name='login'),
    path('register/', register, name='register'),

]