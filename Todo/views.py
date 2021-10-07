from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .serializers import TaskSerializer
from .models import Task
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def apiOverview(request):
	api_urls = { 'List' : '/task-list' ,
		'Create' : '/task-create' ,
		'Update' : '/task-update/<str:pk>/ ' ,
		'Delete' : '/task-delete/<str:pk>/' , }
	return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
	tasks = Task.objects.all()
	serializer = TaskSerializer(tasks,many=True)
	return Response(serializer.data)
	
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def taskcreate(request):
	serializer = TaskSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def taskupdate(request,pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance = task, data = request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
	
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def taskdelete(request,pk):
	task = Task.objects.get(id=pk)
	task.delete()
	return Response("Task Deleted")