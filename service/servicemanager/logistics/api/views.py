from rest_framework import generics, mixins
from logistics.models import Material
from .serializers import MaterialSerializer


class MaterialList(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class MaterialRudView(generics.RetrieveUpdateDestroyAPIView):
  lookup_field      = 'pk'
  queryset          = Material.objects.all()
  serializer_class  = MaterialSerializer
