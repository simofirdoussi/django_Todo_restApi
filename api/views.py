from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'create':'/task-create/',
        'update':'/task-update/<str:pk>/',
        'delete':'/task-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serilizer = TaskSerializer(tasks, many=True)
    return Response(serilizer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serilizer = TaskSerializer(task, many=False)
    return Response(serilizer.data)

@api_view(['POST'])
def taskCreate(request):
    serilizer = TaskSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
    return Response(serilizer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serilizer = TaskSerializer(instance=task,data=request.data)
    if serilizer.is_valid():
        serilizer.save()
    return Response(serilizer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    
    return Response(serilizer.data)