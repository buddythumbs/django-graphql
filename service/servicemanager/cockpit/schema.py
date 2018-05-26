from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType


# Import models from models.py 
from .models import ServiceNotification, Task, KnownIssue, Engineer, Tool, ToolOwner, Category, Shift, ActionPlan


# Define all the types for all models in models.py
class ServiceNotificationType(DjangoObjectType):
    class Meta:
        model = ServiceNotification

class TaskType(DjangoObjectType):
    class Meta:
        model = Task

class KnownIssueType(DjangoObjectType):
    class Meta:
        model = KnownIssue

class EngineerType(DjangoObjectType):
    class Meta:
        model = Engineer

class ToolType(DjangoObjectType):
    class Meta:
        model = Tool

class ToolOwnerType(DjangoObjectType):
    class Meta:
        model = ToolOwner

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class ShiftType(DjangoObjectType):
    class Meta:
        model = Shift

class ActionPlanType(DjangoObjectType):
    class Meta:
        model = ActionPlan

class EngineerType(DjangoObjectType):
    class Meta:
        model = get_user_model()

# Query class
class Query(graphene.ObjectType):
    service_notifications = graphene.List(ServiceNotificationType)
    tasks = graphene.List(TaskType)
    known_issues = graphene.List(KnownIssueType)
    engineers = graphene.List(EngineerType)
    tools = graphene.List(ToolType)
    tool_owners = graphene.List(ToolOwnerType)
    categorys = graphene.List(CategoryType)
    shifts = graphene.List(ShiftType)
    action_plans = graphene.List(ActionPlanType)
    me = graphene.Field(EngineerType)

    def resolve_service_notifications(self, info, **kwargs):
        print(info.context.user)
        return ServiceNotification.objects.all()

    def resolve_tasks(self, info, **kwargs):
        return Task.objects.all()

    def resolve_known_issues(self, info, **kwargs):
        return KnownIssue.objects.all()

    def resolve_engineers(self, info, **kwargs):
        return Engineer.objects.all()

    def resolve_tools(self, info, **kwargs):
        return Tool.objects.all()

    def resolve_tool_owners(self, info, **kwargs):
        return ToolOwner.objects.all()

    def resolve_categorys(self, info, **kwargs):
        return Category.objects.all()

    def resolve_shifts(self, info, **kwargs):
        return Shift.objects.all()

    def resolve_action_plans(self, info, **kwargs):
        return ActionPlan.objects.all()

    def resolve_me(self, info):
        me = info.context.user
        if me.is_anonymous:
            raise Exception('Not logged!')

        return me

# Mutations
# Service notification
class CreateServiceNotification(graphene.Mutation):
    id = graphene.Int()
    description = graphene.String()
    status = graphene.String()
    category = graphene.String()
    create_date = graphene.String()
    creator = graphene.String()

    #2
    class Arguments:
        description = graphene.String()
        status = graphene.String()
        category = graphene.String()

    #3
    def mutate(self, info, category=None, description=""):

        creator = info.context.user
        if creator.is_anonymous:
            raise Exception('Not logged!') 

        if category:
            cat = Category.objects.get(category=category)
        else:
            cat = null
        service_notification = ServiceNotification(
            status = "NEW", 
            description = description, 
            category = cat,
            creator = creator
        )
        service_notification.save()

        return CreateServiceNotification(
            id=service_notification.pk,
            status=service_notification.status,
            description=service_notification.description,
            category=service_notification.category,
            creator=service_notification.creator,
            create_date=service_notification.create_date
        )
# Task
class CreateTask(graphene.Mutation):
    id = graphene.String()
    description = graphene.String()
    status = graphene.String()
    create_date = graphene.String()
    category = graphene.String()
    high_priority = graphene.Boolean()
    owner = graphene.String()
    due_date = graphene.String()

    #2
    class Arguments:
        description = graphene.String(required=True)
        status = graphene.String()
        category = graphene.String()
        owner = graphene.String()
        high_priority = graphene.Boolean()

    #3
    def mutate(self, info, owner, description, high_priority=False, category=None, status="todo"):

        creator = info.context.user
        if creator.is_anonymous:
            raise Exception('Not logged!') 
        print(creator)
        if owner:
            owner = Engineer.objects.get(username=owner)
        else:
            owner = creator
        print(owner)
        if not category is None:
            cat = Category.objects.get(category=category)
        else:
            cat = null
        print(cat) 
        # Create new task object from query paramters 
        task = Task(
            status = status, 
            description = description,
            high_priority = high_priority
        )

        task.save()
        task.owner = owner
        task.category = cat
        task.creator = creator
        task.save()
        

        return CreateTask(
            id = task.pk,
            status = task.status,
            description = task.description,
            category = task.category,
            create_date = task.create_date,
            owner = task.owner,
            high_priority = task.high_priority,
            due_date = task.due_date
        )

# Engineer / User
class CreateEngineer(graphene.Mutation):
    user = graphene.Field(EngineerType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        abbreviation = graphene.String(required=True)
        shift = graphene.String(required=True)


    def mutate(self, info, username, password, email, abbreviation, shift=None):
        
        if shift:
            Shift.objects.get(shift=shift)
        else:
            shift = null
        engineer = get_user_model()(
            username=username,
            abbreviation=abbreviation,
            shift=shift
        )
        engineer.set_password(password)
        engineer.save()

        return CreateEngineer(engineer=engineer)

#4
class Mutation(graphene.ObjectType):
    create_service_notification = CreateServiceNotification.Field()
    create_task = CreateTask.Field()
    create_engineer = CreateEngineer.Field()