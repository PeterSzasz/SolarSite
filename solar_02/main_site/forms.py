from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Project

class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = []