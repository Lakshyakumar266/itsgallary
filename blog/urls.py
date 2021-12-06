from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogHome, name='BlogHome'),
    path('blogpost/<str:slug>', views.BlogPost, name='BlogPost'),
    path('comment', views.BlogComment, name='Comment'),
]