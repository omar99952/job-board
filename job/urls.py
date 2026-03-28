from django.contrib import admin
from django.urls import path ,include
from . import views

app_name = 'job'

urlpatterns = [
    path('',views.get_all_jobs),
    path('<str:slug>',views.get_job_detail,name='job_detail'),
]