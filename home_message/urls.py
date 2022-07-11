from home_message.views import getMessage_view, createMessage_view, updateMessage_view, deleteMessage_view, MessageListAPIView
from django.urls import path

app_name = 'home_message'

urlpatterns = [
    path('create-new', MessageListAPIView.as_view(), name='create-new'),


]