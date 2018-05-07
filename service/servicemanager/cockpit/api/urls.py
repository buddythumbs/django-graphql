from .views import (
  TaskRudView, 
  EngineerRudView, 
  CategoryRudView,
  ShiftRudView, 
  TaskAPIView, 
  EngineerList, 
  CategoryList, 
  ShiftList, 
  ToolRudView, 
  ToolList, 
  ToolOwnerRudView, 
  ToolOwnerList,
  ActionPlanRudView,
  ActionPlanList,
  )

from django.urls import path

urlpatterns = [
  path('tasks/<int:pk>/', TaskRudView.as_view(), name='task-rud'),
  path('tasks/', TaskAPIView.as_view(), name='task-api'),
  path('engineers/<int:pk>/', EngineerRudView.as_view(), name='engineer-rud'),
  path('engineers/', EngineerList.as_view(), name='engineer-api'),
  path('category/<int:pk>/', CategoryRudView.as_view(), name='category-api'),
  path('categorys/', CategoryList.as_view(), name='category-api'),
  path('shifts/<int:pk>/', ShiftRudView.as_view(), name='shift-rud'),
  path('shifts/', ShiftList.as_view(), name='shift-api'),
  path('tools/<int:pk>/', ToolRudView.as_view(), name='tool-rud'),
  path('tools/', ToolList.as_view(), name='tool-api'),
  path('tool-owners/<int:pk>/', ToolOwnerRudView.as_view(), name='tool-owner-rud'),
  path('tool-owners/', ToolOwnerList.as_view(), name='tool-owner-api'),
  path('action-plans/<int:pk>/', ActionPlanRudView.as_view(), name='action-plan-rud'),
  path('action-plans/', ActionPlanList.as_view(), name='action-plan-api'),
]