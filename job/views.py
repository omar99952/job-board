from django.shortcuts import render
from .models import job 
from django.core.paginator import Paginator
# Create your views here.
def get_all_jobs(request):
    all_jobs=job.objects.all()
    paginator = Paginator(all_jobs,1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"jobs": page_obj}
    return render(request,"job/jobs.html",context)

def get_job_detail(request,slug):
    job_detail = job.objects.get(slug=slug)
    context = { "job" :job_detail}
    return render(request,"job/job_detail.html",context)
