from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.searilizers import EmpDataSearilizer
from accounts.models import EmpData

@api_view(['GET'])
def Apioverview(request):
    return Response("API collecting")

@api_view(['GET'])
def Emplist(request):
    emp=EmpData.objects.all()
    searilizer=EmpDataSearilizer(emp,many=True)
    return Response(searilizer.data)
   
@api_view(['POST'])
def Empcreate(request):
    serializer=EmpDataSearilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('item added')

@api_view(['POST'])
def Empupdate(request, pk):
    serializer = EmpData.objects.get(pk=pk)
    data = EmpDataSearilizer(instance=serializer, data=request.data)
    if data.is_valid():
        data.save()
        # return Response('item updated')


@api_view(['DELETE'])
def Empdelete(request, pk):
    serializer = get_object_or_404(EmpData, pk=pk)
    serializer.delete()
    return Response('Item deleted')

@api_view(['GET'])
def Emplistid(request,pk):
    emp=EmpData.objects.get(pk=pk)
    searilizer=EmpDataSearilizer(emp)
    return Response(searilizer.data)
       