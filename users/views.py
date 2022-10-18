
from socket import SIO_KEEPALIVE_VALS
from tkinter.tix import Form
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import customUserCreationForm,Profileform,skillForm
from django.contrib.auth.decorators import login_required
from .models import Profile,skill
from django.db.models import Q
from .utils import searchProfiles, paginateProfiles

# Create your views here.
@login_required(login_url='login')  
def profiles(request):
    profiles, search_query = searchProfiles(request)

    custom_range, profiles = paginateProfiles(request, profiles, 3)
    context = {'profiles': profiles, 'search_query': search_query,
               'custom_range': custom_range}
    return render(request, 'users/profiles.html', context)

@login_required(login_url='login')      
def userprofile(request,pk):
    profiles = Profile.objects.get(id=pk)

    topSkills = profiles.skill_set.exclude(description__exact="")  # type: ignore
    otherSkills = profiles.skill_set.filter(description="")  # type: ignore



    context = {'profiles':profiles, 'topSkills':topSkills, 'otherSkills':otherSkills}
    return render(request, 'users/user-profile.html', context)    
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'username does not exist')  
        user = authenticate(request, username=username,password=password)  

        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,'username or password is incorrect')        
    return render(request, 'users/login_register.html')  
def logoutUser(request):
    logout(request)
    messages.error(request,'user was logged out')
    return redirect('login')   

def registerUser(request):
    page = 'register'
    form = customUserCreationForm()

    if request.method == 'POST':
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('edit-account')

        else:
            messages.success(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)   

@login_required(login_url='login')        
def userAccount(request):
    profile = request.user.profile

    skills = profile.skill_set.all()  # type: ignore
    projects =profile.project_set.all()
    
    context = {'profile':profile, 'skills':skills,'projects':projects }
    return render(request, 'users/account.html', context)
@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = Profileform(instance=profile)

    if request.method == 'POST':
        form = Profileform(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)
@login_required(login_url='login') 
def createSkill(request):
    profile = request.user.profile
    form = skillForm()

    if request.method == 'POST':
        form = skillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'skill was created succesfully!')
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/skill_form.html', context)  

@login_required(login_url='login') 
def updateSkill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = skillForm(instance=skill)

    if request.method == 'POST':
        form = skillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'skill was updated succesfully!')
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/skill_form.html', context)    

def deleteSkill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('account')
    context = {'object': skill}
    return render(request, 'delete_template.html', context)       
  