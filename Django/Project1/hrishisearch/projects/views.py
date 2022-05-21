from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


# Create your views here.

def about(request):
    page = 'projects'
    name = 'junior'
    context = {'page':page,'name':name}
    return render(request,'about/project.html',context)

def project(request):
    page = Project.objects.all()
    name = 'junior'
    context = {'page':page,'name':name}
    return render(request,'projects/project.html',context)