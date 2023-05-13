from django.urls import path

from chat.views import ChatView, get_token_view, print_chats, create_message

urlpatterns = [
    path('', ChatView.as_view(), name='chat'),
    path('token/', get_token_view, name='token'),
    path('chat/', print_chats, name='print_chats'),
    path('sending/', create_message, name='create_message'),
]
