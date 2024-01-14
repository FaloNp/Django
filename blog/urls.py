from django.urls import path
from . import views
from .views import add_post

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add/', add_post, name='add_post'),
]