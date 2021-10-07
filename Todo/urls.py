from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views as v1
from . import views

urlpatterns = [
    path('api-token-auth/', v1.obtain_auth_token),
    path('',views.apiOverview, name = 'Overview'),
    path('task-list/',views.tasklist,name='task-list'),
    path('task-create/',views.taskcreate,name='task-create'),
    path('task-update/<str:pk>',views.taskupdate,name='task-update'),
    path('task-delete/<str:pk>',views.taskdelete,name='task-delete'),
]