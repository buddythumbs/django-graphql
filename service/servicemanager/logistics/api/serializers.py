from rest_framework import serializers
from logistics.models import Material

class MaterialSerializer(serializers.ModelSerializer):
  class Meta:
    model = Material
    fields = [
      'pk',
      'description',
      'NC',
      'serial',
      'addition_date',
      'service_order',
      'location',
      'tool_no',
      'location',
      'status'
    ]