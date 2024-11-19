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

    path('CSM/ballot', views.CSMballot, name='CSMballot'),
    path('CSM/candidates', views.CSMcandidates, name='CSMcandidates'),
    path('CSM/tally', views.CSMtally, name='CSMtally'),
    path('CSM/result', views.CSMresult, name='CSMresult'),
    path('CSM/candidate/update/<str:pk>', views.updateCSMcandidate, name='updateCSMcandidate'),
    path('CSM/candidate/delete/<str:pk>', views.deleteCSMcandidate, name='deleteCSMcandidate'),


    path('CLA/ballot', views.CLAballot, name='CLAballot'),
    path('CLA/candidates', views.CLAcandidates, name='CLAcandidates'),
    path('CLA/tally', views.CLAtally, name='CLAtally'),
    path('CLA/result', views.CLAresult, name='CLAresult'),
    path('CLA/candidate/update/<str:pk>', views.updateCLAcandidate, name='updateCLAcandidate'),
    path('CLA/candidate/delete/<str:pk>', views.deleteCLAcandidate, name='deleteCLAcandidate'),
    
]
