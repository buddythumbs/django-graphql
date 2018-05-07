import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
from django.contrib.postgres.fields import JSONField

class Task(models.Model):
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('Engineer',null=True, blank=True, on_delete=models.SET_NULL)
    due_date = models.DateTimeField()
    duration = models.DecimalField(max_digits=4, decimal_places=1, default=0.5)
    category = models.ForeignKey('Category',null=True, on_delete=models.SET_NULL)
    owner = models.ManyToManyField('Engineer',related_name="ownedtasks")
    service_order = models.CharField(max_length=10, null=True, blank=True)
    related_task = models.ForeignKey("Task",null=True, blank=True, on_delete=models.SET_NULL)
    high_priority =models.NullBooleanField(default=False,null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True, default="todo")


    def __str__(self):
        return self.description

    def due_soon(self):
        return self.due_date <= timezone.now() + datetime.timedelta(days=1)

class ServiceNotification(models.Model):
    """ Container for tasks, action plans and service orders """
    description = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('Engineer',null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey('Category',null=True, on_delete=models.SET_NULL)
    owner = models.ManyToManyField('Engineer',related_name="ownednotifications")
    service_order = models.CharField(max_length=10, null=True, blank=True)
    related_task = models.ManyToManyField("Task",null=True, blank=True)
    related_action_plan = models.ManyToManyField("ActionPlan",null=True, blank=True)
    high_priority =models.NullBooleanField(default=False,null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True, default="todo")


    def __str__(self):
        return self.description

class KnownIssue(models.Model):
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('Engineer',null=True, blank=True, on_delete=models.SET_NULL)
    tool = models.ForeignKey('Tool',null=True, on_delete=models.SET_NULL, related_name="associated_known_issues")


    def __str__(self):
        return self.description

class Engineer(models.Model):
    abbreviation = models.CharField(max_length=4, blank=True)
    shift = models.ForeignKey('Shift',null=True, on_delete=models.SET_NULL, blank=True)
    vacation_hours = models.DecimalField(max_digits=5, decimal_places=2,default=195)
    sap = models.CharField(max_length=10,null=True, blank=True)

    def __str__(self):
        return self.abbreviation 

class ToolOwner(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Shift(models.Model):
    shift = models.CharField(max_length=50)
    sup = models.ForeignKey('Engineer', related_name="boss",blank=True,null=True, on_delete=models.SET_NULL )

    def __str__(self):
        return self.shift  

class Tool(models.Model):
    number = models.CharField(max_length=5)
    customer_name = models.CharField(max_length=10)
    create_date = models.DateTimeField(auto_now_add=True)
    body_type = models.CharField(max_length=20, null=True, blank=True)
    owner = models.ForeignKey('ToolOwner',null=True, blank=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=40, null=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    

    def __str__(self):
        return '{} {}'.format(self.number, self.customer_name)

class ActionPlan(models.Model):
    description = models.CharField(max_length=255)
    reason = models.TextField()
    creator = models.ForeignKey('Engineer',null=True, blank=True, on_delete=models.SET_NULL,related_name="created_action_plans")
    submitter = models.ForeignKey('Engineer',null=True, blank=True, on_delete=models.SET_NULL,related_name="submitted_action_plans")
    reviewer_1st_line = models.ManyToManyField('Engineer', blank=True,related_name="reviewed_action_plans_1st")
    reviewer_2nd_line = models.ManyToManyField('Engineer', blank=True,related_name="reviewed_action_plans_2nd")
    approver = models.ForeignKey('Engineer',null=True, blank=True, on_delete=models.SET_NULL,related_name="approved_action_plans")
    executer = models.ManyToManyField('Engineer',related_name="executed_action_plans", blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    submit_date = models.DateTimeField(null=True, blank=True)
    scheduled_date = models.DateTimeField(null=True, blank=True)
    start_date_time = models.DateTimeField(null=True, blank=True)
    finish_date_time = models.DateTimeField(null=True, blank=True)
    duration = models.DecimalField(max_digits=4, decimal_places=1, default=0.5)
    actual_duration = models.DecimalField(max_digits=4, decimal_places=1, default=0.5)
    b_factor = models.DecimalField(max_digits=4, decimal_places=1, default=1.2)
    actual_b_factor = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    service_order = models.CharField(max_length=10, null=True, blank=True)
    tool = models.ForeignKey('Tool',null=True, on_delete=models.SET_NULL, related_name="associated_action_plans")
    ok_to_run =models.NullBooleanField(default=False,null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True, default="draft")
    content = JSONField(blank=True, null=True)
    materials = models.ManyToManyField('logistics.Material',related_name="associated_cois", blank=True)

    def __str__(self):
        return self.description