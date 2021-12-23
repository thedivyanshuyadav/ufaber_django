from django.shortcuts import render,HttpResponse,redirect
from .models import Project
from .forms import *

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    print(context)
    return render(request,'index.html',context=context)

def add_project(request):
    if request.method=='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    context = {'form':ProjectForm()}
    return render(request,'add_project.html',context=context)

def project_view(request,project_id):
    obj = Project.objects.get(id=project_id)
    tasks = Task.objects.filter(assigned_to=obj)
    print(tasks)
    context = {'project':obj,'tasks':tasks}
    return render(request, 'view_project.html', context=context)

def edit_project(request,project_id):
    obj = Project.objects.get(id=project_id)
    if request.method=="POST":
        form = ProjectForm(request.POST, request.FILES,instance=obj)
        if form.is_valid():
            form.save()
    context = {'form':ProjectForm(instance=obj),'project_id':project_id}
    return render(request,'edit_project.html',context)

def delete_project(request,project_id):
    obj = Project.objects.get(id=project_id)
    obj.delete()
    return redirect('/')



def add_task(request,project_id):
    proj = Project.objects.get(id=project_id)
    if request.method=='POST':
        data = request.POST.dict()
        del data['csrfmiddlewaretoken']
        task = Task.objects.create(**data)
        task.assigned_to = proj
        task.save()
        print(task.assigned_to,'FORM VALID')
    context = {'form':TaskForm(),'project_id':project_id}
    context['form'].assigned_to=proj
    return render(request,'add_task.html',context=context)

def edit_task(request,project_id,task_id):
    task = Task.objects.get(id=task_id)
    if request.method=="POST":
        form = TaskForm(request.POST, request.FILES,instance=task)
        if form.is_valid():
            form.save()
    context = {'form':TaskForm(instance=task),'project_id':project_id}
    return render(request,'edit_task.html',context)

def delete_task(request,project_id,task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/project/'+str(project_id))

def view_task(request,project_id,task_id):
    task = Task.objects.get(id=task_id)
    project_id = task.assigned_to.id
    context = {
        'task':Task.objects.get(id=task_id),
        'project_id':project_id,
    }
    return render(request,'view_task.html',context=context)
