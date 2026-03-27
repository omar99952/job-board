from django.shortcuts import render
from .models import job 
# Create your views here.
def get_all_jobs(request):
    all_jobs=job.objects.all
    context = {"jobs": all_jobs}
    return render(request,"job/jobs.html",context)

def get_job_detail(request,id):
    job_detail = job.objects.get(id=id)
    context = { "job_detail" :job_detail}
    return render(request,"job/job_detail.html",context)
