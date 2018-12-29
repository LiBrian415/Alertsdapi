from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Alert
from app.serializers import AlertSerializer, AlertUpdateSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def alert_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        alerts = Alert.objects.all()
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = AlertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def alert_detail(request, pk):
    """
    Retrieve, update, or delete a code snippet.
    """
    try:
        alert = Alert.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlertSerializer(alert)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AlertUpdateSerializer(alert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        alert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
