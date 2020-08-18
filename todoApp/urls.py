from django.contrib import admin
from django.urls import path, include
from todoApp import views


urlpatterns = [
    path('',views.home, name="home"),
    path('signup/', views.handleSignup, name="signup"),
    path('login/', views.handleLogin, name="login"),
    path('logout/', views.handleLogout, name="logout"),
    path('add/', views.add, name="add"),
    path('save/<str:id>/', views.save, name="save"),
    path('delete/<str:pk>/', views.delete, name="delete"),
    path('edit/<str:pk>/', views.edit, name="edit"),
]