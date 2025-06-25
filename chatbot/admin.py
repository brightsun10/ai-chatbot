from django.contrib import admin
from .models import ChatSession, Message, Feedback


@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'user', 'created_at')
    search_fields = ('session_id', 'user__username')
    list_filter = ('created_at',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('session', 'is_user', 'timestamp', 'short_content')
    list_filter = ('is_user', 'timestamp')
    search_fields = ('content',)

    def short_content(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    short_content.short_description = "Message"


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('message', 'rating', 'submitted_at')
    list_filter = ('rating', 'submitted_at')
    search_fields = ('comment',)
