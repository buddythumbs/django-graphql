from rest_framework import generics, mixins
from cockpit.models import Task, Category, Engineer, Shift, Tool, ToolOwner, ActionPlan
from .serializers import TaskSerializer, EngineerSerializer, CategorySerializer, ShiftSerializer, ToolSerializer, ToolOwnerSerializer, ActionPlanSerializer

class TaskRudView(generics.RetrieveUpdateDestroyAPIView):
  lookup_field      = 'pk'
  queryset          = Task.objects.all()
  serializer_class  = TaskSerializer

class TaskAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
      qs = Task.objects.all()
      query = self.request.GET.get("q")
      if query is not None:
        qs = qs.filter(description__icontains=query)
      return qs

    # def perform_create(self,serializer):
    #   serializer.save(creator=self.request.user.username)
    
    def post(self,request, *args, **kwargs):
      return self.create(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #   return self.create(request, *args, **kwargs)

class EngineerRudView(generics.RetrieveUpdateDestroyAPIView):
  pass
  lookup_field      = 'pk'
  queryset          = Engineer.objects.all()
  serializer_class  = EngineerSerializer

class EngineerList(generics.ListCreateAPIView):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer

class CategoryRudView(generics.RetrieveUpdateDestroyAPIView):
  pass
  lookup_field      = 'pk'
  queryset          = Category.objects.all()
  serializer_class  = CategorySerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ShiftRudView(generics.RetrieveUpdateDestroyAPIView):
  pass
  lookup_field      = 'pk'
  queryset          = Shift.objects.all()
  serializer_class  = ShiftSerializer

class ShiftList(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    
class ToolList(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

class ToolRudView(generics.RetrieveUpdateDestroyAPIView):
  lookup_field      = 'pk'
  queryset          = Tool.objects.all()
  serializer_class  = ToolSerializer

class ToolList(generics.ListCreateAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    
class ToolOwnerRudView(generics.RetrieveUpdateDestroyAPIView):
  lookup_field      = 'pk'
  queryset          = ToolOwner.objects.all()
  serializer_class  = ToolOwnerSerializer

class ToolOwnerList(generics.ListCreateAPIView):
    queryset = ToolOwner.objects.all()
    serializer_class = ToolOwnerSerializer

class ActionPlanList(generics.ListCreateAPIView):
    queryset = ActionPlan.objects.all()
    serializer_class = ActionPlanSerializer

class ActionPlanRudView(generics.RetrieveUpdateDestroyAPIView):
  lookup_field      = 'pk'
  queryset          = ActionPlan.objects.all()
  serializer_class  = ActionPlanSerializer
