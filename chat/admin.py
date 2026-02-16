from django.contrib import admin

from .models import ChatMessage


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "message")
    list_filter = ("created_at", "user")
    search_fields = ("message", "user__username")
