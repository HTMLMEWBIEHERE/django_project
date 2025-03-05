# Description: URL patterns for the tasks app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'), #the home/index page
    path('create/', views.task_create, name='task_create'), #creating a task page
    path('update/<int:pk>/', views.task_update, name='task_update'), #updating a task page
    path('delete/<int:pk>/', views.task_delete, name='task_delete'), #deleting a task page
]