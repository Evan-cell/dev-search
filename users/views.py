
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)
def userprofile(request,pk):
    profiles = Profile.objects.get(id=pk)

    topSkills = profiles.skill_set.exclude(description__exact="")  # type: ignore
    otherSkills = profiles.skill_set.filter(description="")  # type: ignore



    context = {'profiles':profiles, 'topSkills':topSkills, 'otherSkills':otherSkills}
    return render(request, 'users/user-profile.html', context)    
def loginPage(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('username does not exist')  
        user = authenticate(request, username=username,password=password)  

        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            print('username or password is incorrect')        
    return render(request, 'users/login_register.html')  
def logoutUser(request):
    logout(request)
    return redirect('login')      
