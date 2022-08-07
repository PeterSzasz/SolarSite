from datetime import datetime
from django.db import models

class Roles(models.Model):
    name = models.CharField(blank=False, max_length=200)

class User(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.CharField(max_length=200, blank=False)
    password = models.CharField(max_length=200, blank=False)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

class Project(models.Model):
    name = models.CharField(max_length=200, blank=False)
    start_date = models.DateTimeField(default=datetime.now)
    def __str__(self) -> str:
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=200, blank=False)

class Device(models.Model):
    name = models.CharField(max_length=200, blank=False)
    #type, like inverter,etc
    input_voltage = models.IntegerField()
    output_voltage = models.IntegerField()

class user_project(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    pid = models.ForeignKey(Project, on_delete=models.CASCADE)

class project_site(models.Model):
    sid = models.ForeignKey(Site, on_delete=models.CASCADE)
    pid = models.ForeignKey(Project, on_delete=models.CASCADE)

class site_device(models.Model):
    sid = models.ForeignKey(Site, on_delete=models.CASCADE)
    did = models.ForeignKey(Device, on_delete=models.CASCADE)