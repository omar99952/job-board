from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Profile
from .form import Profileform, Signupform, Userform
from django.contrib.auth import authenticate
from django.contrib.auth import login
# Create your views here.
 
def sign_up(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user= authenticate(username=username,passsword=password)
            login(request,user)
            return redirect('accounts/profile/')
    else:
        form = Signupform()
    
    return render(request,'registration/signup.html',{'form':form})
    
    
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})



def edit_profile(request):
    
    profile = Profile.objects.get(user=request.user)
    
    if request.method =='POST':
        user = Userform( request.POST,instance=request.user)
        profile =Profileform(request.POST,request.FILES,instance=profile)
        if user.is_valid() and profile.is_valid():
            user.save()
            profile = profile.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = Userform(instance=request.user) 
        profileform = Profileform(instance=profile)
    
    return render(request,'accounts/edit_profile.html',{'userform':userform ,'profileform':profileform })