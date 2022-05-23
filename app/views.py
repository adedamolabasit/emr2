from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TestSerializer
from .models import Test
# Create your views here.

@api_view(['GET'])
def apioverview(request):
    api_endpoints = {
        'list':'/api/emr-list',
        'Detail View':'/api/emr-detail/<int:pk>/',
        'Create view':'/api/emr-create/',
        'Update':'/api/emr-update/<int:pk>/',
        'Delete':'/api/emr-delete/<int:pk>/',
   }
    return Response(api_endpoints)


@api_view(['GET'])
def emr_list(request):
    tasks = Test.objects.all()
    serializer=TestSerializer(tasks,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def emr_detail(request,pk):
    tasks = Test.objects.get(id=pk)
    serializer=TestSerializer(tasks,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def emr_create(request):
    serializer=TestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['PATCH'])
def emr_update(request,pk):
    tasks=Test.objects.get(id=pk)
    serializer=TestSerializer(instance=tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def emr_delete(request,pk):
    tasks=Test.objects.get(id=pk)
    tasks.delete()
    return Response('Test Deleted Successfully')