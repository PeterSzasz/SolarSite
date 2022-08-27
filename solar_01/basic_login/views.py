from django.shortcuts import get_list_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
from .models import Project

def loginPage(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    valid_user = authenticate(request, username=username, password=password)

    if valid_user is not None:
        login(request, valid_user)
        return redirect('basic_login:dashboard')

    context = {}
    return render(request, 'basic_login/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('basic_login:login')

def registrationPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('basic_login:login')

    context = {'form':form}
    return render(request, 'basic_login/registration.html', context)

def forgotPage(request):
    context = {}
    return render(request, 'basic_login/forgot_pass.html', context)

@login_required(login_url='basic_login:login')
def dashboardPage(request):
    projects = Project.objects.all()
    #projects = get_list_or_404(Project)
    context = {'projects':projects}
    return render(request, 'basic_login/dashboard.html', context)

@login_required(login_url='basic_login:login')
def projectPage(request):
    user = request.user
    projects = None
    if user.id == 1:
        projects = Project.objects.all()
    elif user.properties.role == 'CUSTOMER':
        projects = Project.objects.filter(customer=user.id)
    elif user.properties.role == 'STAFF':
        projects = Project.objects.filter(owner=user.id)
    context = {'projects':projects}
    return render(request, 'basic_login/projects.html', context)