from django.urls import path
from . import views

urlpatterns = [
    path('a/', views.home, name='home'),
    path('download/', views.download, name='download'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]