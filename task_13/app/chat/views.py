from django.shortcuts import render
from django.views.generic import TemplateView

from chat.models import Chat
import json
from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed, HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from chat.serializers import serialize_chat


# Create your views here.

class ChatView(TemplateView):
    template_name = 'chat.html'


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(f'Only GET request are allowed {request.method}')


def print_chats(request, *args, **kwargs):
    messages = Chat.objects.all().order_by('created_at')
    chats = []
    for message in messages:
        result = [serialize_chat(chat=message)]
        chats.append(result)
    response_data = {'chats': chats}
    response = JsonResponse(response_data)
    response.status_code = 200
    return response


@csrf_exempt
def create_message(request, *args, **kwargs):
    json_dict = json.loads(request.body)
    user_id = json_dict.get('user_id')
    message_text = json_dict.get('message')
    user = User.objects.get(id=user_id)
    Chat.objects.create(user_pk=user, text=message_text)
    response_data = {'Chat': 'Сообщение отправлено'}
    response = JsonResponse(response_data)
    response.status_code = 200
    return response
