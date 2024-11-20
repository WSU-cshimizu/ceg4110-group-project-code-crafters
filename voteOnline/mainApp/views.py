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



##############CLA############################
@user_passes_test(lambda u: u.is_superuser)
def CLAcandidates(request):
    candidate_form = CLA_CandidatesForm()
    if request.method == 'POST':
        candidate_form = CLA_CandidatesForm(request.POST, request.FILES)
        if candidate_form.is_valid():
            candidate_form.save()
            return HttpResponseRedirect(reverse("CLAcandidates"))

    context = {
        'title': 'CLA Candidates',
        'form': candidate_form,
        'CLA': CLA_Candidate.objects.all()
    }
    return render(request, 'main/CLA/CLAcandidates.html', context)



@user_passes_test(lambda u: u.is_superuser)
def updateCLAcandidate(request, pk):
    candidate = CLA_Candidate.objects.get(id=pk)
    candidate_form = CLA_CandidatesForm(instance=candidate)
    context = {
        'title': 'Update CLA Candidate',
        'candidate_form': candidate_form
    }
    if request.method == 'POST':
        candidate_form = CLA_CandidatesForm(request.POST, request.FILES, instance=candidate)
        if candidate_form.is_valid():
            candidate_form.save()
            return HttpResponseRedirect(reverse('CLAcandidates'))
    return render(request, 'main/CLA/CLAupdatecandidate.html', context)


@user_passes_test(lambda u: u.is_superuser)
def deleteCLAcandidate(request, pk):
    CLAcandidate = CLA_Candidate.objects.get(id=pk)
    context = {
        'title': 'Delete CLA Candidate',
      'CLAcandidate': CLAcandidate,
    }
    if request.method == 'POST':
        CLAcandidate.delete()
        return HttpResponseRedirect(reverse('CLAcandidates'))

    return render(request, 'main/CLA/CLAdeletecandidate.html', context)


@user_passes_test(lambda u: u.is_superuser)
def CLAtally(request):
    context = {
        'title': 'CLA Tally',
        'CLA': CLA_Candidate.objects.all(),
    }
    return render(request, 'main/CLA/CLAtally.html', context)


@user_passes_test(lambda u: u.is_superuser)
def CLAresult(request):
    context = {
        'title': 'CLA Result',
        'president': CLA_Candidate.objects.filter(position='President'),
        'vicepresident': CLA_Candidate.objects.filter(position='Vice President'),
        'secretary': CLA_Candidate.objects.filter(position='Secretary'),
        'treasurer': CLA_Candidate.objects.filter(position='Treasurer'),
        'eventco': CLA_Candidate.objects.filter(position='Event Coordinator'),
        'srofficer': CLA_Candidate.objects.filter(position='Sports and Recreation Officer'),
        'culturalaffairs': CLA_Candidate.objects.filter(position='Cultural affairs officer'),
        'departmenthead': CLA_Candidate.objects.filter(position='Department Representative'),
    }
    return render(request, 'main/CLA/CLAresult.html', context)



@login_required(login_url='login')
@verified_or_superuser
@CLA_voter_or_superuser
@department_not_voted_or_superuser
@CLA_schedule_or_superuser
def CLAballot(request):
    context = {
        'title': 'CLA Ballot',
        'president': CLA_Candidate.objects.filter(position='President'),
        'vicepresident': CLA_Candidate.objects.filter(position='Vice President'),
        'secretary': CLA_Candidate.objects.filter(position='Secretary'),
        'treasurer': CLA_Candidate.objects.filter(position='Treasurer'),
        'eventco': CLA_Candidate.objects.filter(position='Event Coordinator'),
        'srofficer': CLA_Candidate.objects.filter(position='Sports and Recreation Officer'),
        'culturalaffairs': CLA_Candidate.objects.filter(position='Cultural affairs officer'),
        'departmenthead': CLA_Candidate.objects.filter(position='Department Representative'),
    }
    if request.method == 'POST':
        voter = request.user
        voter.voted_department = True
        voter.save()
        sweetify.success(request, 'Vote Submitted!')
        

    ###### President ######
    try: 
        request.POST['president']
        voted_president = request.POST["president"]
        g_voted = CLA_Candidate.objects.get(fullname=voted_president)
        g_voters = g_voted.voters
        g_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CLA')
        Records.president = voted_president
        Records.save()

    except:
        print("No selected President")
    

    ###### VICE President ######
    try:
        voted_vicepresident = request.POST["vicepresident"]
        vg_voted = CLA_Candidate.objects.get(fullname=voted_vicepresident)
        vg_voters = vg_voted.voters
        vg_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CLA')
        Records.vice_president = voted_vicepresident
        Records.save()


    except:
        print("No selected Vice President")


        ###### Secretary ######
    try:
        voted_secretary = request.POST["secretary"]
        s_voted = CLA_Candidate.objects.get(fullname=voted_secretary)
        s_voters = s_voted.voters
        s_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CLA')
        Records.secretary = voted_secretary
        Records.save()


    except:
        print("No selected Secretary")


            ###### Treasurer ######
    try:
        voted_treasurer = request.POST["treasurer"]
        t_voted = CLA_Candidate.objects.get(fullname=voted_treasurer)
        t_voters = t_voted.voters
        t_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CLA')
        Records.treasurer = voted_treasurer
        Records.save()
        
    except:
        print("No selected Treasurer")


            ###### Event Coordinator ######
    try:
        voted_eventco = request.POST["eventco"]
        a_voted = CLA_Candidate.objects.get(fullname=voted_eventco)
        a_voters = a_voted.voters
        a_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CLA')
        Records.event_coordinator = voted_eventco
        Records.save()
        
    except:
        print("No selected Event Coordinator")


            ###### Sports and Recreation Officer ######
    try:
        voted_srofficer = request.POST["srofficer"]
        p_voted = CLA_Candidate.objects.get(fullname=voted_srofficer)
        p_voters = p_voted.voters
        p_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CLA')
        Records.sports_recreation_officer = voted_srofficer
        Records.save()
        
    except:
        print("No selected Sports and Recreation Officer")


            ###### Cultural Affairs officer ######
    try:
        voted_cula = request.POST["culturalaffairs"]
        b_voted = CLA_Candidate.objects.get(fullname=voted_cula)
        b_voters = b_voted.voters
        b_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CLA')
        Records.cultural_affairs_officer = voted_cula
        Records.save()
        
    except:
        print("No selected Cultural Affairs officer")

    
            ###### Department Representative ######
    try:
        voted_represent = request.POST["departmenthead"]
        p_voted = CLA_Candidate.objects.get(fullname=voted_represent)
        p_voters = p_voted.voters
        p_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CLA')
        Records.departmentrepresentative = voted_represent
        Records.save()
        return HttpResponseRedirect(reverse('Records'))
        
    except:
        print("No selected Department Representative")
    

    return render(request, 'main/CLA/CLAballot.html', context)



#################CSM######################################
@user_passes_test(lambda u: u.is_superuser)
def CSMcandidates(request):
    candidate_form = CSM_CandidatesForm()
    if request.method == 'POST':
        candidate_form = CSM_CandidatesForm(request.POST, request.FILES)
        if candidate_form.is_valid():
            candidate_form.save()
            return HttpResponseRedirect(reverse("CSMcandidates"))

    context = {
        'title': 'CSM Candidates',
        'form': candidate_form,
        'CSM': CSM_Candidate.objects.all()
    }
    return render(request, 'main/CSM/CSMcandidates.html', context)

@user_passes_test(lambda u: u.is_superuser)
def updateCSMcandidate(request, pk):
    candidate = CSM_Candidate.objects.get(id=pk)
    candidate_form = CSM_CandidatesForm(instance=candidate)
    context = {
        'title': 'Update CSM Candidate',
        'candidate_form': candidate_form
    }
    if request.method == 'POST':
        candidate_form = CSM_CandidatesForm(request.POST, request.FILES, instance=candidate)
        if candidate_form.is_valid():
            candidate_form.save()
            return HttpResponseRedirect(reverse('CSMcandidates'))
    return render(request, 'main/CSM/CSMupdatecandidate.html', context)


@user_passes_test(lambda u: u.is_superuser)
def deleteCSMcandidate(request, pk):
    CSMcandidate = CSM_Candidate.objects.get(id=pk)
    context = {
        'title': 'Delete CSM Candidate',
      'CSMcandidate': CSMcandidate,
    }
    if request.method == 'POST':
        CSMcandidate.delete()
        return HttpResponseRedirect(reverse('CSMcandidates'))

    return render(request, 'main/CSM/CSMdeletecandidate.html', context)



@user_passes_test(lambda u: u.is_superuser)
def CSMtally(request):
    context = {
        'title': 'CSM Tally',
        'CSM': CSM_Candidate.objects.all(),
    }
    return render(request, 'main/CSM/CSMtally.html', context)


@user_passes_test(lambda u: u.is_superuser)
def CSMresult(request):
    context = {
        'president': CSM_Candidate.objects.filter(position='President'),
        'vicepresident': CSM_Candidate.objects.filter(position='Vice President'),
        'secretary': CSM_Candidate.objects.filter(position='Secretary'),
        'treasurer': CSM_Candidate.objects.filter(position='Treasurer'),
        'eventco': CSM_Candidate.objects.filter(position='Event Coordinator'),
        'srofficer': CSM_Candidate.objects.filter(position='Sports and Recreation Officer'),
        'culturalaffairs': CSM_Candidate.objects.filter(position='Cultural affairs officer'),
        'departmenthead': CSM_Candidate.objects.filter(position='Department Representative'),
    }
    return render(request, 'main/CSM/CSMresult.html', context)



@login_required(login_url='login')
@verified_or_superuser
@CSM_voter_or_superuser
@department_not_voted_or_superuser
@CSM_schedule_or_superuser
def CSMballot(request):
    context = {
        'title': 'CSM Ballot',
        'president': CSM_Candidate.objects.filter(position='President'),
        'vicepresident': CSM_Candidate.objects.filter(position='Vice President'),
        'secretary': CSM_Candidate.objects.filter(position='Secretary'),
        'treasurer': CSM_Candidate.objects.filter(position='Treasurer'),
        'eventco': CSM_Candidate.objects.filter(position='Event Coordinator'),
        'srofficer': CSM_Candidate.objects.filter(position='Sports and Recreation Officer'),
        'culturalaffairs': CSM_Candidate.objects.filter(position='Cultural affairs officer'),
        'departmenthead': CSM_Candidate.objects.filter(position='Department Representative'),
    }
    if request.method == 'POST':
        voter = request.user
        voter.voted_department = True
        voter.save()
        sweetify.success(request, 'Vote Submitted!')
        

    ###### President ######
    try: 
        request.POST['president']
        voted_president = request.POST["president"]
        g_voted = CSM_Candidate.objects.get(fullname=voted_president)
        g_voters = g_voted.voters
        g_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CSM')
        Records.president = voted_president
        Records.save()

    except:
        print("No selected President")
    

    ###### VICE President ######
    try:
        voted_vicepresident = request.POST["vicepresident"]
        vg_voted = CSM_Candidate.objects.get(fullname=voted_vicepresident)
        vg_voters = vg_voted.voters
        vg_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CSM')
        Records.vice_president = voted_vicepresident
        Records.save()


    except:
        print("No selected Vice President")


        ###### Secretary ######
    try:
        voted_secretary = request.POST["secretary"]
        s_voted = CSM_Candidate.objects.get(fullname=voted_secretary)
        s_voters = s_voted.voters
        s_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CSM')
        Records.secretary = voted_secretary
        Records.save()


    except:
        print("No selected Secretary")


            ###### Treasurer ######
    try:
        voted_treasurer = request.POST["treasurer"]
        t_voted = CSM_Candidate.objects.get(fullname=voted_treasurer)
        t_voters = t_voted.voters
        t_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CSM')
        Records.treasurer = voted_treasurer
        Records.save()
        
    except:
        print("No selected Treasurer")


            ###### Event Coordinator ######
    try:
        voted_eventco = request.POST["eventco"]
        a_voted = CSM_Candidate.objects.get(fullname=voted_eventco)
        a_voters = a_voted.voters
        a_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CSM')
        Records.event_coordinator = voted_eventco
        Records.save()
        
    except:
        print("No selected Event Coordinator")


            ###### Sports and Recreation Officer ######
    try:
        voted_srofficer = request.POST["srofficer"]
        p_voted = CSM_Candidate.objects.get(fullname=voted_srofficer)
        p_voters = p_voted.voters
        p_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CSM')
        Records.sports_recreation_officer = voted_srofficer
        Records.save()
        
    except:
        print("No selected Sports and Recreation Officer")


            ###### Cultural Affairs Officer ######
    try:
        voted_cult = request.POST["culturalaffairs"]
        b_voted = CSM_Candidate.objects.get(fullname=voted_cult)
        b_voters = b_voted.voters
        b_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CSM')
        Records.cultural_affairs_officer = voted_cult
        Records.save()
        
    except:
        print("No selected Cultural Affairs Officer")

    
            ###### Department Representative ######
    try:
        voted_departrep = request.POST["departmenthead"]
        p_voted = CSM_Candidate.objects.get(fullname=voted_departrep)
        p_voters = p_voted.voters
        p_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CSM')
        Records.departmentrepresentative = voted_departrep
        Records.save()
        return HttpResponseRedirect(reverse('Records'))
        
    except:
        print("No selected Department Representative")


    return render(request, 'main/CSM/CSMballot.html', context)


#################CECS############################
@user_passes_test(lambda u: u.is_superuser)
def CECScandidates(request):
    candidate_form = CECS_CandidatesForm()
    if request.method == 'POST':
        candidate_form = CECS_CandidatesForm(request.POST, request.FILES)
        if candidate_form.is_valid():
            candidate_form.save()
            return HttpResponseRedirect(reverse("CECScandidates"))

    context = {
        'title': 'CECS Candidates',
        'form': candidate_form,
        'CECS': CECS_Candidate.objects.all()
    }
    return render(request, 'main/CECS/CECScandidates.html', context) 

@user_passes_test(lambda u: u.is_superuser)
def updateCECScandidate(request, pk):
    candidate = CECS_Candidate.objects.get(id=pk)
    candidate_form = CECS_CandidatesForm(instance=candidate)
    context = {
                'title': 'Update CECS Candidate',
                'candidate_form': candidate_form
    }
    if request.method == 'POST':
        candidate_form = CECS_CandidatesForm(request.POST, request.FILES, instance=candidate)
        if candidate_form.is_valid():
            candidate_form.save()
            return HttpResponseRedirect(reverse('CECScandidates'))
    return render(request, 'main/CECS/CECSupdatecandidate.html', context)


@user_passes_test(lambda u: u.is_superuser)
def deleteCECScandidate(request, pk):
    CECScandidate = CECS_Candidate.objects.get(id=pk)
    context = {
        'title': 'Delete CECS Candidate',
        'CECScandidate': CECScandidate,
    }
    if request.method == 'POST':
        CECScandidate.delete()
        return HttpResponseRedirect(reverse('CECScandidates'))

    return render(request, 'main/CECS/CECSdeletecandidate.html', context)



@user_passes_test(lambda u: u.is_superuser)
def CECStally(request):
    context = {
        'title': 'CECS Tally',
        'CECS': CECS_Candidate.objects.all(),
    }
    return render(request, 'main/CECS/CECStally.html', context)


@user_passes_test(lambda u: u.is_superuser)
def CECSresult(request):
    context = {
        'title': 'CECS Result',
        'president': CECS_Candidate.objects.filter(position='President'),
        'vicepresident': CECS_Candidate.objects.filter(position='Vice President'),
        'secretary': CECS_Candidate.objects.filter(position='Secretary'),
        'treasurer': CECS_Candidate.objects.filter(position='Treasurer'),
        'eventco': CECS_Candidate.objects.filter(position='Event Coordinator'),
        'srofficer': CECS_Candidate.objects.filter(position='Sports and Recreation Officer'),
        'culturalaffairs': CECS_Candidate.objects.filter(position='Cultural affairs officer'),
        'departmenthead': CECS_Candidate.objects.filter(position='Department Representative'),
    }
    return render(request, 'main/CECS/CECSresult.html', context)



@login_required(login_url='login')
@verified_or_superuser
@CECS_voter_or_superuser
@department_not_voted_or_superuser
@CECS_schedule_or_superuser
def CECSballot(request):
    context = {
        'title': 'CECS Ballot',
        'president': CECS_Candidate.objects.filter(position='President'),
        'vicepresident': CECS_Candidate.objects.filter(position='Vice President'),
        'secretary': CECS_Candidate.objects.filter(position='Secretary'),
        'treasurer': CECS_Candidate.objects.filter(position='Treasurer'),
        'eventco': CECS_Candidate.objects.filter(position='Event Coordinator'),
        'srofficer': CECS_Candidate.objects.filter(position='Sports and Recreation Officer'),
        'culturalaffairs': CECS_Candidate.objects.filter(position='Cultural affairs officer'),
        'departmenthead': CECS_Candidate.objects.filter(position='Department Representative'),
    }
    if request.method == 'POST':
        voter = request.user
        voter.voted_department = True
        voter.save()
        sweetify.success(request, 'Vote Submitted!')


    ###### President ######
    try: 
        request.POST['president']
        voted_president = request.POST["president"]
        g_voted = CECS_Candidate.objects.get(fullname=voted_president)
        g_voters = g_voted.voters
        g_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CECS')
        Records.president = voted_president
        Records.save()

    except:
        print("No selected President")
    

    ###### VICE President ######
    try:
        voted_vicepresident = request.POST["vicepresident"]
        vg_voted = CECS_Candidate.objects.get(fullname=voted_vicepresident)
        vg_voters = vg_voted.voters
        vg_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CECS')
        Records.vice_president = voted_vicepresident
        Records.save()


    except:
        print("No selected Vice President")


        ###### Secretary ######
    try:
        voted_secretary = request.POST["secretary"]
        s_voted = CECS_Candidate.objects.get(fullname=voted_secretary)
        s_voters = s_voted.voters
        s_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CECS')
        Records.secretary = voted_secretary
        Records.save()


    except:
        print("No selected Secretary")


            ###### Treasurer ######
    try:
        voted_treasurer = request.POST["treasurer"]
        t_voted = CECS_Candidate.objects.get(fullname=voted_treasurer)
        t_voters = t_voted.voters
        t_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CECS')
        Records.treasurer = voted_treasurer
        Records.save()
        
    except:
        print("No selected Treasurer")


            ###### Event Coordinator ######
    try:
        voted_event_co = request.POST["eventco"]
        a_voted = CECS_Candidate.objects.get(fullname=voted_event_co)
        a_voters = a_voted.voters
        a_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CECS')
        Records.event_coordinator = voted_event_co
        Records.save()
        
    except:
        print("No selected Event Coordinator")


            ###### Sports and Recreation Officer ######
    try:
        voted_srofficer = request.POST["srofficer"]
        p_voted = CECS_Candidate.objects.get(fullname=voted_srofficer)
        p_voters = p_voted.voters
        p_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CECS')
        Records.sports_recreation_officer = voted_srofficer
        Records.save()
        
    except:
        print("No selected Sports and Recreation Officer")


            ###### Cultural Affairs Officer ######
    try:
        voted_culturalaffairs = request.POST["culturalaffairs"]
        b_voted = CECS_Candidate.objects.get(fullname=voted_culturalaffairs)
        b_voters = b_voted.voters
        b_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CECS')
        Records.cultural_affairs_officer = voted_culturalaffairs
        Records.save()
        
    except:
        print("No selected Cultural Affairs Officer")

    
            ###### Department Head ######
    try:
        voted_departmenthead = request.POST["departmenthead"]
        p_voted = CECS_Candidate.objects.get(fullname=voted_departmenthead)
        p_voters = p_voted.voters
        p_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='CECS')
        Records.departmenthead = voted_departmenthead
        Records.save()
        return HttpResponseRedirect(reverse('Records'))
        
    except:
        print("No selected Department Head")


    return render(request, 'main/CECS/CECSballot.html', context)



############################## CBUS ############################################


@user_passes_test(lambda u: u.is_superuser)
def CBUScandidates(request):
    candidate_form = CBUS_CandidatesForm()
    if request.method == 'POST':
        candidate_form = CBUS_CandidatesForm(request.POST, request.FILES)
        if candidate_form.is_valid():
            candidate_form.save()
            return HttpResponseRedirect(reverse("CBUScandidates"))

    context = {
        'title': 'CBUS Candidates',
        'form': candidate_form,
        'CBUS': CBUS_Candidate.objects.all()
    }
    return render(request, 'main/CBUS/CBUScandidates.html', context)


@user_passes_test(lambda u: u.is_superuser)
def updateCBUScandidate(request, pk):
    candidate = CBUS_Candidate.objects.get(id=pk)
    candidate_form = CBUS_CandidatesForm(instance=candidate)
    context = {
        'title': 'Update CBUS Candidate',
        'candidate_form': candidate_form
    }
    if request.method == 'POST':
        candidate_form = CBUS_CandidatesForm(request.POST, request.FILES, instance=candidate)
        if candidate_form.is_valid():
            candidate_form.save()
            return HttpResponseRedirect(reverse('CBUScandidates'))
    return render(request, 'main/CBUS/CBUSupdatecandidate.html', context)


@user_passes_test(lambda u: u.is_superuser)
def deleteCBUScandidate(request, pk):
    CBUScandidate = CBUS_Candidate.objects.get(id=pk)
    context = {
        'title': 'Delete CBUS Candidate',
        'CBUScandidate': CBUScandidate,
    }
    if request.method == 'POST':
        CBUScandidate.delete()
        return HttpResponseRedirect(reverse('CBUScandidates'))

    return render(request, 'main/CBUS/CBUSdeletecandidate.html', context)



@user_passes_test(lambda u: u.is_superuser)
def CBUStally(request):
    context = {
        'title': 'CBUS Tally',
        'CBUS': CBUS_Candidate.objects.all(),
    }
    return render(request, 'main/CBUS/CBUStally.html', context)


@user_passes_test(lambda u: u.is_superuser)
def CBUSresult(request):
    context = {
        'title': 'CBUS Result',
        'president': CBUS_Candidate.objects.filter(position='President'),
        'vicepresident': CBUS_Candidate.objects.filter(position='Vice President'),
        'secretary': CBUS_Candidate.objects.filter(position='Secretary'),
        'treasurer': CBUS_Candidate.objects.filter(position='Treasurer'),
        'eventco': CBUS_Candidate.objects.filter(position='Event Coordinator'),
        'srofficer': CBUS_Candidate.objects.filter(position='Sports and Recreation Officer'),
        'culturalaffairs': CBUS_Candidate.objects.filter(position='Cultural affairs officer'),
        'departmenthead': CBUS_Candidate.objects.filter(position='Department Representative'),

    }
    return render(request, 'main/CBUS/CBUSresult.html', context)



@login_required(login_url='login')
@verified_or_superuser
@CBUS_voter_or_superuser
@department_not_voted_or_superuser
@CBUS_schedule_or_superuser
def CBUSballot(request):
    context = {
        'title': 'CBUS Ballot',
        'president': CBUS_Candidate.objects.filter(position='President'),
        'vicepresident': CBUS_Candidate.objects.filter(position='Vice President'),
        'secretary': CBUS_Candidate.objects.filter(position='Secretary'),
        'treasurer': CBUS_Candidate.objects.filter(position='Treasurer'),
        'eventco': CBUS_Candidate.objects.filter(position='Event Coordinator'),
        'srofficer': CBUS_Candidate.objects.filter(position='Sports and Recreation Officer'),
        'culturalaffairs': CBUS_Candidate.objects.filter(position='Cultural affairs officer'),
        'departmenthead': CBUS_Candidate.objects.filter(position='Department Representative'),
    }
    if request.method == 'POST':
        voter = request.user
        voter.voted_department = True
        voter.save()
        sweetify.success(request, 'Vote Submitted!')      
        

    ###### president ######
    try: 
        request.POST['president']
        voted_president = request.POST["president"]
        g_voted = CBUS_Candidate.objects.get(fullname=voted_president)
        g_voters = g_voted.voters
        g_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department="CBUS")
        Records.president = voted_president
        Records.save()

    except:
        print("No selected president")
    

    ###### VICE president ######
    try:
        voted_vicepresident = request.POST["vicepresident"]
        vg_voted = CBUS_Candidate.objects.get(fullname=voted_vicepresident)
        vg_voters = vg_voted.voters
        vg_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department="CBUS")
        Records.vice_president = voted_vicepresident
        Records.save()


    except:
        print("No selected Vice president")


        ###### Secretary ######
    try:
        voted_secretary = request.POST["secretary"]
        s_voted = CBUS_Candidate.objects.get(fullname=voted_secretary)
        s_voters = s_voted.voters
        s_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department="CBUS")
        Records.secretary = voted_secretary
        Records.save()


    except:
        print("No selected Secretary")


            ###### Treasurer ######
    try:
        voted_treasurer = request.POST["treasurer"]
        t_voted = CBUS_Candidate.objects.get(fullname=voted_treasurer)
        t_voters = t_voted.voters
        t_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department="CBUS")
        Records.treasurer = voted_treasurer
        Records.save()
        
    except:
        print("No selected Treasurer")


            ###### Event Coordinator ######
    try:
        voted_eventco = request.POST["eventco"]
        a_voted = CBUS_Candidate.objects.get(fullname=voted_eventco)
        a_voters = a_voted.voters
        a_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department="CBUS")
        Records.event_coordinator = voted_eventco
        Records.save()
        
    except:
        print("No selected Event Coordinator")


            ###### Sports Recreation Officer ######
    try:
        voted_srofficer = request.POST["srofficer"]
        p_voted = CBUS_Candidate.objects.get(fullname=voted_srofficer)
        p_voters = p_voted.voters
        p_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department="CBUS")
        Records.sports_recreation_officer = voted_srofficer
        Records.save()
        
    except:
        print("No selected Sports Recreation Officer")


            ###### Cultural Affairs Officer ######
    try:
        voted_culturalaffairs = request.POST["culturalaffairs"]
        b_voted = CBUS_Candidate.objects.get(fullname=voted_culturalaffairs)
        b_voters = b_voted.voters
        b_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department="CBUS")
        Records.cultural_affairs_officer = voted_culturalaffairs
        Records.save()
        
    except:
        print("No selected Cultural Affairs Officer")

    
            ###### Department Representative ######
    try:
        voted_represent = request.POST["departmenthead"]
        p_voted = CBUS_Candidate.objects.get(fullname=voted_represent)
        p_voters = p_voted.voters
        p_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department="CBUS")
        Records.departmentrepresentative = voted_represent
        Records.save()
        return HttpResponseRedirect(reverse('Records'))
        
    except:
        print("No selected Department Representative")


    return render(request, 'main/CBUS/CBUSballot.html', context)





######## MAIN WSU section #####################

@user_passes_test(lambda u: u.is_superuser)
def maincandidates(request):
    candidate_form = MAIN_CandidatesForm()
    if request.method == 'POST':
        candidate_form = MAIN_CandidatesForm(request.POST, request.FILES)
        if candidate_form.is_valid():
            candidate_form.save()
            return HttpResponseRedirect(reverse("maincandidates"))

    context = {
        'title': 'Main WSU Candidates',
        'form': candidate_form,
        'main': MAIN_Candidate.objects.all()
    }
    return render(request, 'main/WSU/maincandidates.html', context)


@user_passes_test(lambda u: u.is_superuser)
def updatemaincandidate(request, pk):
    candidate = MAIN_Candidate.objects.get(id=pk)
    candidate_form = MAIN_CandidatesForm(instance=candidate)
    context = {
                'title': 'Update Main WSU Candidate',
                'candidate_form': candidate_form
    }
    if request.method == 'POST':
        candidate_form = MAIN_CandidatesForm(request.POST, request.FILES, instance=candidate)
        if candidate_form.is_valid():
            candidate_form.save()
            return HttpResponseRedirect(reverse('maincandidates'))
    return render(request, 'main/WSU/mainupdatecandidate.html', context)


@user_passes_test(lambda u: u.is_superuser)
def deletemaincandidate(request, pk):
    maincandidate = MAIN_Candidate.objects.get(id=pk)
    context = {
        'title': 'Delete Main WSU Candidate',
      'maincandidate': maincandidate,
    }
    if request.method == 'POST':
        maincandidate.delete()
        return HttpResponseRedirect(reverse('maincandidates'))

    return render(request, 'main/WSU/maindeletecandidate.html', context)



@user_passes_test(lambda u: u.is_superuser)
def maintally(request):
    context = {
        'title': 'Main WSU Tally',
        'main': MAIN_Candidate.objects.all(),
    }
    return render(request, 'main/WSU/maintally.html', context)


@user_passes_test(lambda u: u.is_superuser)
def mainresult(request):
    context = {
        'title': 'Main WSU Result',
        'president': MAIN_Candidate.objects.filter(position='President'),
        'vicepresident': MAIN_Candidate.objects.filter(position='Vice President'),
        'secretary': MAIN_Candidate.objects.filter(position='Secretary'),
        'treasurer': MAIN_Candidate.objects.filter(position='Treasurer'),
        'eventco': MAIN_Candidate.objects.filter(position='Event Coordinator'),
        'srofficer': MAIN_Candidate.objects.filter(position='Sports and Recreation Officer'),
        'culturalaffairs': MAIN_Candidate.objects.filter(position='Cultural affairs officer'),
        'departmenthead': MAIN_Candidate.objects.filter(position='Department Representative'),


    }
    return render(request, 'main/WSU/mainresult.html', context)



@login_required(login_url='login')
@verified_or_superuser
@main_schedule_or_superuser
@main_not_voted_or_superuser
def mainballot(request):
    context = {
        'title': 'Main WSU Ballot',
        'president': MAIN_Candidate.objects.filter(position='President'),
        'vicepresident': MAIN_Candidate.objects.filter(position='Vice President'),
        'secretary': MAIN_Candidate.objects.filter(position='Secretary'),
        'treasurer': MAIN_Candidate.objects.filter(position='Treasurer'),
        'eventco': MAIN_Candidate.objects.filter(position='Event Coordinator'),
        'srofficer': MAIN_Candidate.objects.filter(position='Sports and Recreation Officer'),
        'culturalaffairs': MAIN_Candidate.objects.filter(position='Cultural affairs officer'),
        'departmenthead': MAIN_Candidate.objects.filter(position='Department Representative'),
    }
    if request.method == 'POST':
        voter = request.user
        voter.voted_main = True
        voter.save()
        sweetify.success(request, 'Vote Submitted!')
        
        

     ###### president ######
    try: 
        request.POST['president']
        voted_president = request.POST["president"]
        g_voted = MAIN_Candidate.objects.get(fullname=voted_president)
        g_voters = g_voted.voters
        g_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='Main Branch')
        Records.president = voted_president
        Records.save()

    except:
        print("No selected president")
    

    ###### VICE president ######
    try:
        voted_vicepresident = request.POST["vicepresident"]
        vg_voted = MAIN_Candidate.objects.get(fullname=voted_vicepresident)
        vg_voters = vg_voted.voters
        vg_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='Main Branch')
        Records.vice_president = voted_vicepresident
        Records.save()


    except:
        print("No selected Vice president")


        ###### Secretary ######
    try:
        voted_secretary = request.POST["secretary"]
        s_voted = MAIN_Candidate.objects.get(fullname=voted_secretary)
        s_voters = s_voted.voters
        s_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='Main Branch')
        Records.secretary = voted_secretary
        Records.save()


    except:
        print("No selected Secretary")


            ###### Treasurer ######
    try:
        voted_treasurer = request.POST["treasurer"]
        t_voted = MAIN_Candidate.objects.get(fullname=voted_treasurer)
        t_voters = t_voted.voters
        t_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='Main Branch')
        Records.treasurer = voted_treasurer
        Records.save()
        
    except:
        print("No selected Treasurer")


            ###### Event Coordinator ######
    try:
        voted_eventco = request.POST["eventco"]
        a_voted = MAIN_Candidate.objects.get(fullname=voted_eventco)
        a_voters = a_voted.voters
        a_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='Main Branch')
        Records.event_coordinator = voted_eventco
        Records.save()
        
    except:
        print("No selected Event Coordinator")


            ###### Sports and Recreation officer ######
    try:
        voted_srofficer = request.POST["srofficer"]
        p_voted = MAIN_Candidate.objects.get(fullname=voted_srofficer)
        p_voters = p_voted.voters
        p_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='Main Branch')
        Records.sports_recreation_officer = voted_srofficer
        Records.save()
        
    except:
        print("No selected Sports and Recreation officer")


            ###### Cultural Affairs Officer ######
    try:
        voted_affairs = request.POST["culturalaffairs"]
        b_voted = MAIN_Candidate.objects.get(fullname=voted_affairs)
        b_voters = b_voted.voters
        b_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='Main Branch')
        Records.cultural_affairs_officer = voted_affairs
        Records.save()
        
    except:
        print("No selected Cultural Affairs Officer")

    
            ###### Department Representative ######
    try:
        voted_depart = request.POST["departmenthead"]
        p_voted = MAIN_Candidate.objects.get(fullname=voted_depart)
        p_voters = p_voted.voters
        p_voters.add(voter)
        Records = UserRecords.objects.get(owner=voter, department='Main Branch')
        Records.departmentrepresentative = voted_depart
        Records.save()
        return HttpResponseRedirect(reverse('Records'))
        
    except:
        print("No selected Department Representative")


    return render(request, 'main/WSU/mainballot.html', context)




















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