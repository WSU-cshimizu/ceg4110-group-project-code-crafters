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
