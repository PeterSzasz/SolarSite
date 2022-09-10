from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CreateProjectForm
from .models import Project

@login_required(login_url='email_login:login')
def dashboardPage(request):
    projects = Project.objects.all()
    #projects = get_list_or_404(Project)
    context = {'projects':projects}
    return render(request, 'main_site/dashboard.html', context)

@login_required(login_url='email_login:login')
def newprojectPage(request):
    form = CreateProjectForm()

    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_site:dashboard')

    context = {'form': form}
    return render(request, 'main_site/new_project.html', context)

@login_required(login_url='email_login:login')
def projectPage(request):
    user = request.user
    projects = None
    if user.id == 1:
        projects = Project.objects.all().order_by("-due_date")
    elif user.properties.role == 'CUSTOMER':
        projects = Project.objects.filter(customer=user.id).order_by("-due_date")
    elif user.properties.role == 'STAFF':
        projects = Project.objects.filter(owner=user.id).order_by("-due_date")
    context = {'projects':projects}
    return render(request, 'main_site/projects.html', context)