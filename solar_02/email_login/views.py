from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm

def loginPage(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    valid_user = authenticate(request, username=username, password=password)

    if valid_user is not None:
        login(request, valid_user)
        return redirect('email_login:dashboard')

    context = {}
    return render(request, 'email_login/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('email_login:login')

def registrationPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('email_login:login')

    context = {'form':form}
    return render(request, 'email_login/registration.html', context)

def forgotPage(request):
    context = {}
    return render(request, 'email_login/forgot_pass.html', context)