from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('Records', views.userRecords, name='Records'),
    
    path('profile/<str:pk>', views.profile, name='profile'),

    path('voters', views.voters, name='voters'),
    path('voters/update/<str:pk>', views.updatevoter, name='updatevoter'),
    path('voters/delete/<str:pk>', views.deletevoter, name='deletevoter'),

    
]
