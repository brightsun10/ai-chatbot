from django.db import models
from django.contrib.auth.models import User


class ChatSession(models.Model):
    """
    Stores a chatbot session for a specific user or anonymous user.
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    session_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session {self.session_id} - User: {self.user}"


class Message(models.Model):
    """
    Stores each message in a chat session.
    """
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    is_user = models.BooleanField(default=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        speaker = "User" if self.is_user else "Bot"
        return f"{speaker} @ {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"


class Feedback(models.Model):
    """
    Optional: Stores user feedback about bot responses.
    """
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, 'Bad'), (2, 'Okay'), (3, 'Good')])
    comment = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for Message ID {self.message.id}"
