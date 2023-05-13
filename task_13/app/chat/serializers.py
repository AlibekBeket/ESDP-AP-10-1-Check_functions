from rest_framework import serializers

from chat.models import Chat


def serialize_user(user):
    return {
        'id': user.id,
        'username': user.username
    }


def serialize_chat(chat):
    return {
        'id': chat.id,
        'message': chat.text,
        'created_at': chat.created_at,
        'user': serialize_user(user=chat.user_pk)
    }
