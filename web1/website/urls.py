from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('',views.home,name='home'),

    path('about/', views.about),
    path('gallery/', views.gallery),
    path('login/', views.login,name='login'),
    path('register', views.signup, name='register'),

]
