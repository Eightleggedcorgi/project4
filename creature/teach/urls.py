from django.contrib import admin

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('index/<int:creatures_id>/', views.creature_detail, name='show'),
    path('create/', views.CreaturesCreate.as_view(), name='create'),
    path('index/<int:pk>/update/', views.CreaturesUpdate.as_view(), name='update'),
    path('index/<int:pk>/delete/', views.CreaturesDelete.as_view(), name='delete'),
]