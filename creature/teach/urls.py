from django.contrib import admin

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('index/<int:creatures_id>/', views.creature_detail, name='show'),
]