from django.shortcuts import render



def landingpage(request):
    return render(request, 'landingpage.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

