from django.shortcuts import render, redirect
from .forms import ProjectForm

# Create your views here.
from gestionForm.models import Project


def project_index(request):
    projects = Project.objects.all()
    return render(request, 'project/index.html', {"projects": projects})


def project_create(request):
    project = Project()
    form = ProjectForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('project.index')
    return render(request, 'project/create.html', {"project": project})


def project_edit(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(request.POST, instance=project)
    if form.is_valid():
        form.save()
        return redirect('project.index')
    return render(request, 'project/create.html', {"project": project})


def project_delete(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('project.index')


def formulario2(request):
    return render(request, 'form2.html')


def formulario3(request):
    return render(request, 'form3.html')


def formulario4(request):
    return render(request, 'form4.html')


def formulario5(request):
    return render(request, 'form5.html')


def home(request):
    return render(request, "home.html")
