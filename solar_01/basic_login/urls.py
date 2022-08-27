from django.urls import path

from . import views

app_name = 'basic_login'
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('registration/', views.registrationPage, name='registration'),
    path('forgot/', views.forgotPage, name='forgot_pass'),
    path('', views.dashboardPage, name='dashboard'),
    path('projects', views.projectPage, name='projects')
]