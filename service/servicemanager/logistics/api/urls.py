from django.urls import path

from .views import MaterialRudView, MaterialList

urlpatterns = [
  path('materials/<int:pk>/', MaterialRudView.as_view(), name='action-plan-rud'),
  path('materials/', MaterialList.as_view(), name='action-plan-api'),
]