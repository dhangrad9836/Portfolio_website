from django.shortcuts import render
from .models import Project, Skill

def home(request):
    projects = Project.objects.all()[:3]  # Get top 3 projects
    skills = Skill.objects.all()
    
    context = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'portfolio/home.html', context)