from django.shortcuts import render

from Project.models import Project


# Create your views here.


def home(req):
    return render(req, 'homepage.html')


def project(req):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(req, 'project_page.html', context)
