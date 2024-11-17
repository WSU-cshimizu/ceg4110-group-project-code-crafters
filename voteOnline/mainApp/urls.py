from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('Records', views.userRecords, name='Records'),
    path('settings', views.settings, name='settings'),
    path('profile/<str:pk>', views.profile, name='profile'),

    path('voters', views.voters, name='voters'),
    path('voters/update/<str:pk>', views.updatevoter, name='updatevoter'),
    path('voters/delete/<str:pk>', views.deletevoter, name='deletevoter'),

    path('election/schedule', views.electionschedule, name='electionschedule'),
    path('election/schedule/update/<str:pk>', views.updateelectionschedule, name='updateelectionschedule'),
    path('election/schedule/delete/<str:pk>', views.deleteelectionschedule, name='deleteelectionschedule'),
    
]
