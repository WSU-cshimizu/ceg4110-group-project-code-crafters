from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from userAccounts.models import *
from .forms import *
import sweetify
from userAccounts.forms import *
from mainApp.decorators import *



def landingpage(request):
    return render(request, 'landingpage/landingpage.html')  


@login_required(login_url='login')
def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'main/home.html', context)

@login_required(login_url='login')
@verified_or_superuser
@Records_exist
def userRecords(request):
    context = {
        'title': 'Records',
        'Records': UserRecords.objects.filter(owner=request.user)

    }
    return render(request, 'main/Records.html', context)

@user_passes_test(lambda u: u.is_superuser)
def voters(request):
    context = {
        'title': 'Voters',
        'voters': Account.objects.filter(is_superuser=False)
    }
    return render(request, 'main/voters.html', context)


@user_passes_test(lambda u: u.is_superuser)
def updatevoter(request, pk):
    voter = Account.objects.get(id=pk)
    voterform = RegistrationForm(instance=voter)
    if request.method == 'POST':
        voterform = RegistrationForm(request.POST, instance=voter)
        if voterform.is_valid():
            voterform.save()
            return HttpResponseRedirect(reverse('voters'))

    context = {
        'title': 'Update Voter',
        'voter': voter,
        'form': voterform,
    }
    
    return render(request, 'main/voterupdate.html', context)



@user_passes_test(lambda u: u.is_superuser)
def deletevoter(request, pk):
    voter = Account.objects.get(id=pk)
    context = {
        'title': 'Delete Voter',
        'voter': voter,
    }
    if request.method == 'POST':
        voter.delete()
        return HttpResponseRedirect(reverse('voters'))
    return render(request, 'main/voterdelete.html', context)



@login_required(login_url='login')
@verified_or_superuser
def profile(request, pk):
    profile = Account.objects.get(id=pk)
    student_form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        student_form = UpdateProfileForm(request.POST, instance=profile)
        password1 = request.POST['password']
        password2 = request.POST['password2']
        if password1 != password2:
            print("password does not match")
            sweetify.error(request, 'Password does not match!')
            return HttpResponseRedirect(request.path_info)
        elif student_form.is_valid():
            student_form.save()
            sweetify.success(request, 'Updated Successfully')
            return HttpResponseRedirect(reverse('login'))
        else: 
            sweetify.error(request, 'Invalid Credentials!')
            return HttpResponseRedirect(request.path_info)
    context = {
        'title': 'Profile',
        'student_form': student_form,
        'profile': profile,
    }
    return render(request, 'main/profile.html', context)

@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    maincandidates =  MAIN_Candidate.objects.all().count()
    CECScandidates = CECS_Candidate.objects.all().count()
    CSMcandidates = CSM_Candidate.objects.all().count()
    CLAcandidates = CLA_Candidate.objects.all().count()
    CBUScandidates = CBUS_Candidate.objects.all().count()
    totalcandidates = maincandidates + CECScandidates + CSMcandidates + CLAcandidates + CBUScandidates
    voted_department = Account.objects.filter(voted_department=True).count()
    voted_main = Account.objects.filter(voted_main=True).count()
    context = {
        'title': 'Dashboard',

        'totalcandidates': totalcandidates,

        'main': MAIN_Candidate.objects.all(),
        'maincandidates': maincandidates,

        'CECS': CECS_Candidate.objects.all(),
        'CECScandidates': CECScandidates,

        'CSM': CSM_Candidate.objects.all(),
        'CSMcandidates': CSMcandidates,

        'CLA': CLA_Candidate.objects.all(),
        'CLAcandidates': CLAcandidates,

        'CBUS': CBUS_Candidate.objects.all(),
        'CBUScandidates': CBUScandidates,
        
        'registered': Account.objects.filter(is_superuser=False).count(),
        'voted': voted_department + voted_main,
    }
    return render(request, 'main/dashboard.html', context)


@user_passes_test(lambda u: u.is_superuser)
def electionschedule(request):
    schedule_form = ScheduleForm()
    if request.method == 'POST':
        schedule_form = ScheduleForm(request.POST)
        if schedule_form.is_valid():
            schedule_form.save()
            return HttpResponseRedirect(reverse('electionschedule'))
    context = {
        'title': 'Schedule',
        'schedule': votingschedule.objects.all(),
        'schedule_form': schedule_form,
    }
    return render(request, 'main/electionschedule.html', context)


@user_passes_test(lambda u: u.is_superuser)
def updateelectionschedule(request, pk):
    schedule = votingschedule.objects.get(id=pk)
    schedule_form = UpdateScheduleForm(instance=schedule)
    context = {
        'title': 'Update Schedule',
        'schedule': schedule,
        'schedule_form': schedule_form
    }
    if request.method == 'POST':
        schedule_form = UpdateScheduleForm(request.POST, instance=schedule)
        if schedule_form.is_valid():
            schedule_form.save()
            return HttpResponseRedirect(reverse('electionschedule'))
    return render(request, 'main/updateelectionschedule.html', context)


@user_passes_test(lambda u: u.is_superuser)
def deleteelectionschedule(request, pk):
    schedule = votingschedule.objects.get(id=pk)
    context = {
        'title': 'Delete Shedule',
        'schedule': schedule,
    }
    if request.method == 'POST':
        schedule.delete()
        return HttpResponseRedirect(reverse('electionschedule'))
    return render(request, 'main/deleteschedule.html', context)


























# SETTINGS
@user_passes_test(lambda u: u.is_superuser)
def settings(request):
    if request.method == 'POST':
        ### MAIN ####
        try:
            if 'reset_main' in request.POST:
                candidates = MAIN_Candidate.objects.all()
                for candidate in candidates:
                    for voter in candidate.voters.all():
                        voter.voted_department = False
                        voter.save()

                    candidate.voters.clear()

                sweetify.toast(request, 'Main WSU Election successfully reset!')
        except:
            print('Cannot Reset Main Branch')


        try:
            if 'delete_main' in request.POST:
                candidates = MAIN_Candidate.objects.all()
                for candidate in candidates:

                    for voter in candidate.voters.all():
                        voter.voted_department = False
                        voter.save()
                    
                    candidate.delete()
                sweetify.toast(request, 'Main WSU Candidates successfully deleted!')
        except:
            print('Cannot Delete Main Branch')

        
        ### CECS ####

        try:
            if 'reset_CECS' in request.POST:
                candidates = CECS_Candidate.objects.all()
                print("CECS running")
                for candidate in candidates:
                    print("CECS running2")
                    for voter in candidate.voters.all():
                        voter.voted_department = False
                        print(f"vote is {voter.voted_department}")
                        voter.save()
                    candidate.voters.clear()
                sweetify.toast(request, 'CECS Election successfully reset!')
        except Exception as e:
            print(f'Cannot Reset CECS Department: {e}')



        try:
            if 'delete_CECS' in request.POST:
                candidates = CECS_Candidate.objects.all()
                for candidate in candidates:

                    for voter in candidate.voters.all():
                        voter.voted_department = False
                        voter.save()
                    
                    candidate.delete()

                sweetify.toast(request, 'CECS Candidates successfully deleted!')
        except:
            print('Cannot Delete CECS Department')


        
        ### CSM ####

        try:
            if 'reset_CSM' in request.POST:
                candidates = CSM_Candidate.objects.all()
                for candidate in candidates:
                    for voter in candidate.voters.all():
                        voter.voted_department = False
                        voter.save()
                    candidate.voters.clear()
                sweetify.toast(request, 'CSM Election successfully reset!')
        except:
            print('Cannot Reset CSM Department')
        try:
            if 'delete_CSM' in request.POST:
                candidates = CSM_Candidate.objects.all()
                for candidate in candidates:

                    for voter in candidate.voters.all():
                        voter.voted_department = False
                        voter.save()

                    candidate.delete()

                sweetify.toast(request, 'CSM Candidates successfully deleted!')
        except:
            print('Cannot Delete CSM Department')


        
        ### CLA ####

        try:
            if 'reset_CLA' in request.POST:
                candidates = CLA_Candidate.objects.all()
                for candidate in candidates:
                    for voter in candidate.voters.all():
                        voter.voted_department = False
                        voter.save()
                    
                    candidate.voters.clear()
                    
                    
                sweetify.toast(request, 'CLA Election successfully reset!')
        except:
            print('Cannot Reset CLA Department')
        try:
            if 'delete_CLA' in request.POST:
                candidates = CLA_Candidate.objects.all()
                for candidate in candidates:
                    

                    for voter in candidate.voters.all():
                        voter.voted_department = False
                        voter.save()

                    candidate.delete()
                sweetify.toast(request, 'CLA Candidates successfully deleted!')
        except:
            print('Cannot Delete CLA Department')

        
        ### CBUS ####
        
        try:
            if 'reset_CBUS' in request.POST:
                candidates = CBUS_Candidate.objects.all()
                for candidate in candidates:
                    

                    for voter in candidate.voters.all():
                        voter.voted_department = False
                        voter.save()

                    candidate.voters.clear()

                sweetify.toast(request, 'CBUS Election successfully reset!')
        except:
            print('Cannot Reset CBUS Department')
        try:
            if 'delete_CBUS' in request.POST:
                candidates = CBUS_Candidate.objects.all()
                for candidate in candidates:
                    

                    for voter in candidate.voters.all():
                        voter.voted_department = False
                        voter.save()
                    
                    candidate.delete()

                sweetify.toast(request, 'CBUS Candidates successfully deleted!')
        except:
            print('Cannot Delete CBUS Department')
        

    context = {
        'title': 'Settings'
    }
    return render(request, 'main/settings.html', context)