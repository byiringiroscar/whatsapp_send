from rest_framework import serializers
from home_message.models import MessageSend


class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageSend
        fields = ['title', 'message', ]