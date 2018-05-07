from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:task_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:task_id>/comments/', views.comments, name='comments'),
]