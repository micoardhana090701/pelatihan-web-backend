from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest, HttpResponse
from myprojectapp.models import Task, Tool
from django.core.files.uploadedfile import SimpleUploadedFile

def tambahtugas(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        image_file = request.FILES['image']
        image_name = image_file.name
        task = Task.objects.create(title=title, description=description, image=SimpleUploadedFile(image_name, image_file.read()))
        task.save()
        return redirect('app:task')
    return render(request, 'taskform.html')

def makanan(request):
    teks = "Ini makanan"
    return HttpResponse(teks)

def task(request):
    tasks = Task.objects.all()
    return render(request, 'tasklist.html', {'tasks': tasks})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image_file = request.FILES['image'] if 'image' in request.FILES else task.image
        task.title = title
        task.description = description
        image_name = image_file.name
        task.image = image_name
        task.save()
        return redirect('app:task')
    return render(request, 'taskedit.html', {'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('app:task')

def tool(request):
    tool = Tool.objects.all()
    return render(request, 'toollist.html', {'tool': tool})

def tambah_tool(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        image_file = request.FILES['image']
        image_name = image_file.name
        task = Tool.objects.create(title=title, description=description, image=SimpleUploadedFile(image_name, image_file.read()))
        task.save()
        return redirect('app:tool')
    return render(request, 'toolform.html')

def tool_delete(request, pk):
    tool = get_object_or_404(Tool, id=pk)
    tool.delete()
    return redirect('app:tool')

def tool_update(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image_file = request.FILES['image'] if 'image' in request.FILES else tool.image
        tool.title = title
        tool.description = description
        image_name = image_file.name
        tool.image = image_name
        tool.save()
        return redirect('app:tool')
    return render(request, 'tooledit.html', {'tool': tool})