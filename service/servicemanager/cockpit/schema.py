# servicemanager/cockpit/schema.py
from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from cockpit.models import (
    Engineer, 
    Task, 
    Category, 
    Shift, 
    ActionPlan,
    Tool, 
    ToolOwner,
    ServiceNotification
    )

class ServiceNotification(DjangoObjectType):
    class Meta:
        model = ServiceNotification
        filter_fields = {
            'description': ['exact', 'icontains', 'istartswith'],
            'category': ['exact'],
            'owner': ['exact'],
        }
        interfaces = (relay.Node, )

class Engineer(DjangoObjectType):
    class Meta:
        model = Engineer
        filter_fields = {
            'abbreviation': ['exact'],
            'shift': ['exact'],
        }
        interfaces = (relay.Node, )

class Task(DjangoObjectType):
    class Meta:
        model = Task
        filter_fields = {
            'description': ['exact', 'icontains', 'istartswith'],
            'category': ['exact'],
            'owner': ['exact'],
        }
        interfaces = (relay.Node, )

class Category(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = {
            'category': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )

class Shift(DjangoObjectType):
    class Meta:
        model = Shift
        filter_fields = {
            'shift': ['exact'],
        }
        interfaces = (relay.Node, )

class Tool(DjangoObjectType):
    class Meta:
        model = Tool
        filter_fields = {
            'number': ['exact'],
            'customer_name': ['exact'],
            'body_type': ['exact'],
        }
        interfaces = (relay.Node, )

class ActionPlan(DjangoObjectType):
    class Meta:
        model = ActionPlan
        filter_fields = {
            'description': ['icontains'],
            'reason': ['icontains'],
            'service_order': ['exact'],
            'ok_to_run': ['exact'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )

class Query(ObjectType):
    notifications = DjangoFilterConnectionField(ServiceNotification)
    notification = relay.Node.Field(ServiceNotification)
    engineers = DjangoFilterConnectionField(Engineer)
    engineer = relay.Node.Field(Engineer)
    tasks = DjangoFilterConnectionField(Task)
    task = relay.Node.Field(Task)
    categories = DjangoFilterConnectionField(Category)
    category = relay.Node.Field(Category)
    shifts = DjangoFilterConnectionField(Shift)
    shift = relay.Node.Field(Shift)
    tools = DjangoFilterConnectionField(Tool)
    tool = relay.Node.Field(Tool)
    actionPlans = DjangoFilterConnectionField(ActionPlan)
    actionPlan = relay.Node.Field(ActionPlan)