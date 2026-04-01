from django.contrib import admin
from django.urls import path ,include
from . import views,api

app_name = 'job'

urlpatterns = [
    path('',views.get_all_jobs,name= 'job_list'),
    path('add',views.add_job,name='add_job'),
    path('<str:slug>',views.get_job_detail,name='job_detail'),
    
    ##api 
    path('api/list',api.get_alljobs,name= 'get_alljobs'),  
    
    
]