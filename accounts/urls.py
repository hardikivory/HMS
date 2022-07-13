
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('nav/', views.NavView),
    path('', views.HomeView, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('guest/changepassword/link/', views.GuestChangePasswordLinkView, name='guest_change_password_link'),
    path('guest/changepassword/', views.GuestChangePasswordView, name='change_password'),
    path('guest/dashboard/', views.GuestDashboardView, name='guest_dashboard'),
    path('guest/update/<int:id>', views.GuestUpdateView, name='guest_update'),
    path('guest/delete/', views.GuestDeleteView, name='guest_delete'),
    path('worker/changepassword/link/', views.WorkerChangePasswordLinkView, name='worker_change_password_link'),
    path('worker/changepassword/', views.WorkerChangePasswordView, name='change_password'),
    path('worker/dashboard/', views.WorkerDashboardView, name='worker_dashboard'),
    path('worker/update/<int:id>', views.WorkerUpdateView, name='worker_update'),  
    path('worker/delete/', views.WorkerDeleteView, name='worker_delete'),  
    path('room/', views.RoomView, name='room'),    
    path('room/book/<int:room_no>', views.RoomBookView, name='roombook'),    
    path('fees/', views.FeesView, name='fees'),    
    path('about/', views.AboutView, name='about'),    
    path('contact/', views.ContactView, name='contact'),    

]
