from django.shortcuts import render
from projects.models import Projects


def project_index(request):
    projects = Projects.objects.all()
    context = {
        'projects' : projects
    }
    return render(request, 'project_index.html', context)