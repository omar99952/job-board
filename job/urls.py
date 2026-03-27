from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('',views.get_all_jobs),
    path('<int:id>',views.get_job_detail),
]