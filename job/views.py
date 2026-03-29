from django.shortcuts import redirect, render
from django.urls import reverse
from .models import job 
from django.core.paginator import Paginator
from .form import Applyform ,Jobform
# Create your views here.
def get_all_jobs(request):
    all_jobs=job.objects.all()
    paginator = Paginator(all_jobs,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"jobs": page_obj ,"real_jobs": all_jobs}
    return render(request,"job/jobs.html",context)

def get_job_detail(request,slug):
    job_detail = job.objects.get(slug=slug)

    if request.method == 'POST':
        form = Applyform(request.POST , request.FILES)
        
        if form.is_valid:
            saved_form = form.save(commit=False)
            saved_form.job = job_detail
            saved_form.save()
    else: form = Applyform() 

    context = { "job" :job_detail , 'form' : form}
    return render(request,"job/job_detail.html",context)

def add_job(request):
   if request.method == 'POST':
    job_form = Jobform(request.POST , request.FILES)
    if job_form.is_valid():
       myform = job_form.save(commit=False)
       myform.owner = request.user
       myform.save()
       return redirect(reverse('jobs:job_list'))

   else: job_form = Jobform()
        

   return render(request ,'job/add_job.html',{"job_form" :job_form})
