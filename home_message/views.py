from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from home_message.models import MessageSend
from home_message.serializer import SendMessageSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions


# Create your views here.

# send message ================== api
class MessageListAPIView(ListCreateAPIView):
    serializer_class = SendMessageSerializer
    queryset = MessageSend.objects.all()

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()



@api_view(['GET', ])
def getMessage_view(request, slug):
    try:
        message_post = MessageSend.objects.get(title=slug)
    except MessageSend.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = SendMessageSerializer(message_post)
        return Response(serializer.data)


@api_view(['PUT', ])
def updateMessage_view(request, slug):
    try:
        message_post = MessageSend.objects.get(title=slug)
    except MessageSend.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = SendMessageSerializer(message_post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successfully"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def deleteMessage_view(request, slug):
    try:
        message_post = MessageSend.objects.get(title=slug)
    except MessageSend.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        operation = message_post.delete()
        data = {}
        if operation:
            data["success"]: "delete successfully"
        else:
            data['failure'] = "delete failed"
        return Response(data=data)


@api_view(['POST', ])
def createMessage_view(request):
    if request.method == "POST":
        serializer = SendMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



