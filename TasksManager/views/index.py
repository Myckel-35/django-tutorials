from TasksManager.models import Project
from django.shortcuts import render

def page(req):
    all_projects = Project.objects.all()
    vars = {'action': "Display all projects",
            'all_projects': all_projects}
    return render(req, 'en/public/index.html', vars)
