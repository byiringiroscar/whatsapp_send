from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone
from home_message.models import MessageSend
from home_message.utilis import send_whatsapp_message


@receiver(post_save, sender=MessageSend)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        message_title = instance.title
        message_body = instance.message
        message = f'{message_title} \n----------------- \n {message_body}'
        send_whatsapp_message(message)
