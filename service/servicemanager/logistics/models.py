from django.db import models

import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser


class Material(models.Model):
    description = models.CharField(max_length=255)
    NC = models.CharField(max_length=15)
    serial = models.CharField(max_length=40)
    addition_date = models.DateTimeField(auto_now_add=True)
    service_order = models.CharField(max_length=10, null=True, blank=True)
    tool_no = models.ForeignKey('cockpit.Tool',null=True, on_delete=models.SET_NULL, related_name="known_issues")
    location = models.CharField(max_length=15)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return '{} {}'.format(self.NC, self.description)
