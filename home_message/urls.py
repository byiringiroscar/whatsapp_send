from home_message.views import MessageListAPIView, sendMessageGroup,  taskWhatsappCreate
from django.urls import path

app_name = 'home_message'

urlpatterns = [
    path('create-new', MessageListAPIView.as_view(), name='create-new'),
    path("send-message", sendMessageGroup, name="send-message"),
    # path('whatsap-send', taskWhatsappCreate, name="whatsapp_create")


]