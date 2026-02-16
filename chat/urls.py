from django.urls import path

from . import views

urlpatterns = [
    path("send/", views.send_message, name="chat_send"),
    path("messages/", views.get_messages, name="chat_messages"),
]
