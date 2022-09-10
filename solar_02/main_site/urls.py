from django.urls import path

from . import views

app_name = 'main_site'
urlpatterns = [
    path('', views.dashboardPage, name='dashboard'),
    path('projects', views.projectPage, name='projects'),
    path('newproject', views.newprojectPage, name='new_project')

]