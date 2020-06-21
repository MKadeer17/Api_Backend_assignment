from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    mem = Members.objects.all()
    serializer = MemberSerializer(mem, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    mem = Members.objects.get(id=pk)
    serializer = MemberSerializer(mem, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    mem = Members.objects.get(id=pk)
    serializer = MemberSerializer(data=request.data, instance=mem)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    mem = Members.objects.get(id=pk)
    mem.delete()
    return Response("Item Successfully Deleted")
