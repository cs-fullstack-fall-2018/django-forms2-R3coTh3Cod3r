from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/edit/', views.edit, name='edit'),
    path('post/new/', views.newpost, name='newpost'),
    path('post/detail/', views.detail, name='detail'),

]