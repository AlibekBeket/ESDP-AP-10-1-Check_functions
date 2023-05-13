from django.db import models
from django.contrib.auth import get_user_model


class Chat(models.Model):
    user_pk = models.ForeignKey(
        verbose_name='Пользователь',
        to=get_user_model(),
        related_name='user',
        blank=False,
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name='Текст сообщения',
        max_length=20000,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата отправки',
        auto_now_add=True
    )

    def __str__(self):
        return f'user id {self.user_pk} - created at {self.created_at}'
