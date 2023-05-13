from django.contrib import admin

from chat.models import Chat


class ChatAdmin(admin.ModelAdmin):
    list_display = ("id", "user_pk", "text", "created_at")
    list_filter = ("id", "user_pk", "text", "created_at")
    search_fields = ("id", "user_pk", "text", "created_at")
    fields = ("user_pk", "text")
    readonly_fields = ("id", "created_at")


admin.site.register(Chat, ChatAdmin)
