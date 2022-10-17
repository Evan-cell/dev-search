import profile
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import project,Tag
from .forms import projectForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

def singleproject(request,pk):
    projectobj = project.objects.get(id=pk)
    tags = projectobj.tags.all
    context={'projectobj':projectobj, 'tas': tags}
    print('projectobj',projectobj)
    return render(request, 'projects/single-project.html', context)

def projects(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        print('search:',search_query)
    projects = project.objects.distinct().filter(
        Q(title__icontains = search_query) 
        )
   
    context = {'projects': projects}
    return render(request, 'projects.html' , context)  
@login_required(login_url="login")
def createproject(request):
    profile = request.user.profile
    form = projectForm()
    if request.method == 'POST':
        form = projectForm(request.POST, request.FILES)
        if form.is_valid:
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'project_form.html', context)  
@login_required(login_url="login")  
def updateproject(request,pk):
    profile = request.user.profile
    projects = profile.project_set.get(id=pk)
    form = projectForm(instance=projects)
  
    if request.method == 'POST':
        form = projectForm(request.POST,request.FILES, instance=projects)
        if form.is_valid:
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'project_form.html', context)    
@login_required(login_url="login")
def deleteproject(request,pk):
    profile = request.user.profile
    projects = profile.project_set.get(id=pk)
    if request.method == 'POST':
        projects.delete()
        return redirect('/')
    context = {'object': projects}
    return render(request, 'delete_template.html', context)       


    
