from django.conf import settings
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Properties(models.Model):
    CUSTOMER = 'CUSTOMER'
    STAFF = 'STAFF'
    ROLES = [
                (CUSTOMER, 'Customer'),
                (STAFF, 'Staff'),
            ]
    role = models.CharField(max_length=100, choices=ROLES, default=CUSTOMER)
    #profile_image = models.ImageField(...)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='properties')

class Project(models.Model):
    name = models.CharField(max_length=200, blank=False)
    start_date = models.DateTimeField(default=datetime.now)
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='project_customer')
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='project_owner')
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