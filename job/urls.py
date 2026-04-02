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
        ## class based view 
    path('api/v2/list',api.JoblistView.as_view(),name= 'JoblistView'),
    path('api/v2/job_detail/<int:id>',api.Job_detail.as_view(),name= 'Job_detail'),
]