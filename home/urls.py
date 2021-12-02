from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='home'),
    path('contact/', views.contact, name='home'),
    path('imagedetail/<str:image_name>', views.ImageView, name='home'),
]
