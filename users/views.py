
from django.shortcuts import render
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
