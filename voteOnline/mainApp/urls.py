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
    
    path('main', views.mainballot, name='main'),
    path('main/candidates', views.maincandidates, name='maincandidates'),
    path('main/tally', views.maintally, name='maintally'),
    path('main/result', views.mainresult, name='mainresult'),
    path('main/candidate/update/<str:pk>', views.updatemaincandidate, name='updatemaincandidate'),
    path('main/candidate/delete/<str:pk>', views.deletemaincandidate, name='deletemaincandidate'),

    path('CECS/ballot', views.CECSballot, name='CECSballot'),
    path('CECS/candidates', views.CECScandidates, name='CECScandidates'),
    path('CECS/tally', views.CECStally, name='CECStally'),
    path('CECS/result', views.CECSresult, name='CECSresult'),
    path('CECS/candidate/update/<str:pk>', views.updateCECScandidate, name='updateCECScandidate'),
    path('CECS/candidate/delete/<str:pk>', views.deleteCECScandidate, name='deleteCECScandidate'),


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


    path('CBUS/ballot', views.CBUSballot, name='CBUSballot'),
    path('CBUS/candidates', views.CBUScandidates, name='CBUScandidates'),
    path('CBUS/tally', views.CBUStally, name='CBUStally'),
    path('CBUS/result', views.CBUSresult, name='CBUSresult'),
    path('CBUS/candidate/update/<str:pk>', views.updateCBUScandidate, name='updateCBUScandidate'),
    path('CBUS/candidate/delete/<str:pk>', views.deleteCBUScandidate, name='deleteCBUScandidate'),
    
]
