from django.shortcuts import render
from django.http import HttpResponse
from projects_page.models import PROJECT_TABLE

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def projects(request):
    projects = PROJECT_TABLE.objects.all()
    context = {'projects': projects }
    return render(request, 'projects_page/projects-page.html', context)

def project(request, pk):
    
    projectObj = PROJECT_TABLE.objects.get(id=pk)
    tags = projectObj.tags.all()
    context = {'projectObj': projectObj, 'tags': tags}
    return render(request, 'projects_page/single-project.html', context)