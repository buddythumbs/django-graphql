from rest_framework import serializers
from cockpit.models import (
  Task, 
  Engineer, 
  Category, 
  Shift, 
  Tool, 
  ToolOwner,
  ActionPlan,
  KnownIssue)

class TaskSerializer(serializers.ModelSerializer):

  creator = serializers.StringRelatedField(many=False)
  category = serializers.StringRelatedField(many=False)
  owner = serializers.StringRelatedField(many=True)

  class Meta:
    model = Task
    fields = [
      'pk',
      'description',
      'creator',
      'owner',
      'create_date',
      'due_date',
      'duration',
      'category',
      'service_order',
      'related_task',
      'high_priority',
      'status'
    ]
    read_only_fields = ['']

class KnownIssuesSerializer(serializers.ModelSerializer):
  creator = serializers.StringRelatedField(many=False)
  tool = serializers.StringRelatedField(many=False)
  class Meta:
    model = KnownIssue
    fields = [
      'pk',
      'description',
      'creator',
      'create_date',
      'tool'
    ]
    read_only_fields = ['']
  
class EngineerSerializer(serializers.ModelSerializer):

  shift = serializers.StringRelatedField(many=False)
  created_action_plans = serializers.StringRelatedField(many=True)
  submitted_action_plans = serializers.StringRelatedField(many=True)
  reviewed_action_plans_1st = serializers.StringRelatedField(many=True)
  reviewed_action_plans_2nd = serializers.StringRelatedField(many=True)
  approved_action_plans = serializers.StringRelatedField(many=True)
  executed_action_plans = serializers.StringRelatedField(many=True)
  ownedtasks = serializers.StringRelatedField(many=True)
  boss = serializers.StringRelatedField(many=False)


  class Meta:
    model = Engineer
    fields = [
      'pk',
      'abbreviation',
      'shift',
      'vacation_hours',
      'sap',
      'created_action_plans',
      'submitted_action_plans',
      'reviewed_action_plans_1st',
      'reviewed_action_plans_2nd',
      'approved_action_plans',
      'executed_action_plans',
      'ownedtasks',
      'boss'
    ]

  def validate_abbreviation(self,value):
    e = Engineer.objects.filter(abbreviation__exact=value)
    if self.instance:
      e = e.exclude(pk=self.instance.pk)
    if(e.exists()):
      raise serializers.ValidationError("Abbreviation must be unique, user already exists.")
    return value
  
  def validate_sap(self,value):
    e = Engineer.objects.filter(sap__exact=value)
    if self.instance:
      e = e.exclude(pk=self.instance.pk)
    if(e.exists()):
      raise serializers.ValidationError("SAP number must be unique, user already exists.")
    return value
    
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = [
      'pk',
      'category',
    ]

class ShiftSerializer(serializers.ModelSerializer):

  sup = serializers.StringRelatedField(many=False)
  

  class Meta:
    model = Shift
    fields = [
      'pk',
      'shift',
      'sup'
    ]

class ToolOwnerSerializer(serializers.ModelSerializer):
  class Meta:
    model = ToolOwner
    fields = [
      'pk',
      'firstname',
      'lastname',
      'email',
    ]

class ToolSerializer(serializers.ModelSerializer):

  associated_action_plans = serializers.StringRelatedField(many=True)
  known_issues = serializers.StringRelatedField(many=True)
  

  class Meta:
    model = Tool
    fields = [
      'pk',
      'number',
      'customer_name',
      'create_date',
      'body_type',
      'owner',
      'location',
      'ip_address',
      'associated_action_plans',
      'known_issues'
    ]

class ActionPlanSerializer(serializers.ModelSerializer):

  creator = EngineerSerializer(many=False)
  submitter = serializers.StringRelatedField(many=False)
  executer = serializers.StringRelatedField(many=True)
  reviewer_1st_line = serializers.StringRelatedField(many=False)
  reviewer_2nd_line = serializers.StringRelatedField(many=False)
  approver = serializers.StringRelatedField(many=False)
  tool = serializers.StringRelatedField(many=False)
  materials = serializers.StringRelatedField(many=True)

  class Meta:
    model = ActionPlan
    fields = [
      'pk',
      'description',
      'reason',
      'creator',
      'submitter',
      'executer',
      'reviewer_1st_line',
      'reviewer_2nd_line',
      'approver',
      'create_date',
      'submit_date',
      'scheduled_date',
      'start_date_time',
      'finish_date_time',
      'duration',
      'actual_duration',
      'b_factor',
      'actual_b_factor',
      'service_order',
      'tool',
      'ok_to_run',
      'content',
      'status',
      'materials'
    ]
    read_only_fields = ['']