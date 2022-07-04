
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.NavView),
    path('home/', views.HomeView),
    path('register/', views.RegisterView),

]
