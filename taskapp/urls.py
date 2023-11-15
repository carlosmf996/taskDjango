from django.urls import path
from . import views
from .views import TaskList, TaskDetails, New

urlpatterns = [
    path('',TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetails.as_view(), name='task_details'),
    path('new', New.as_view(), name='new'),
]