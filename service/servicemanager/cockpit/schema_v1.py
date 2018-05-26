# servicemanager/cockpit/schema.py
import graphene
from graphene import relay, ObjectType, AbstractType, InputObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from cockpit.helpers.graphql_helpers import get_errors, get_object, update_create_instance

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

class ServiceNotificationCreateInput(InputObjectType):
    """
    Class defined to accept input data 
    from the interactive graphql console.
    """
    description = graphene.String(required=False)
    category = graphene.String(required=False)
    status = graphene.String(required=False)

class CreateServiceNotification(relay.ClientIDMutation):
  
    class Input:
        # ServiceNotificationCreateInput class used as argument here.
        service_notification = graphene.Argument(ServiceNotificationCreateInput)

    new_service_notification = graphene.Field(ServiceNotification)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):

        service_notification_data = input.get('service_notification') # get the service notification input from the args
        service_notification = ServiceNotification() # get an instance of the service notification model here
        new_service_notification = update_create_instance(service_notification, service_notification_data) # use custom function to create service notification

        return cls(new_service_notification=new_service_notification) # newly created service notification instance returned.

class UpdateServiceNotification(relay.ClientIDMutation):

    class Input:
        service_notification = graphene.Argument(ServiceNotificationCreateInput) # get the service notification input from the args
        id = graphene.String(required=True) # get the service notification id

    errors = graphene.List(graphene.String)
    updated_book = graphene.Field(ServiceNotification)

    @classmethod
    def mutate_and_get_payload(cls, args, context, info):

        try:
            service_notification_instance = get_object(ServiceNotification, args['id']) # get service notification by id
            if service_notification_instance:
                # modify and update service notification model instance
                service_notofication_data = args.get('service_notification')
                updated_service_notification = update_create_instance(service_notification_instance, service_notofication_data)
                return cls(updated_service_notification=updated_service_notification)
        except ValidationError as e:
            # return an error if something wrong happens
            return cls(updated_service_notification=None, errors=get_errors(e))

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


class Mutation(ObjectType):
    create_service_notification = CreateServiceNotification.Field()     
    update_service_notification = UpdateServiceNotification.Field()