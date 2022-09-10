from django.db import models
from datetime import datetime
from django.db import models
from django.conf import settings


class Device(models.Model):
    name = models.CharField(max_length=200, blank=False)
    input_voltage = models.IntegerField()
    output_voltage = models.IntegerField()
    def __str__(self) -> str:
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=200, blank=False)
    devices = models.ManyToManyField(Device, related_name='device')
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200, blank=False)
    start_date = models.DateTimeField(default=datetime.now)
    due_date = models.DateTimeField(default=datetime.now)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='project_customer')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='project_owner')
    sites = models.ManyToManyField(Site, related_name='site')
    def __str__(self) -> str:
        return self.name