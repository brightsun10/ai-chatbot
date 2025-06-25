import uuid
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatSession, Message, Feedback
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
import json


def get_or_create_session(request):
    session_id = request.session.get('chat_session_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        request.session['chat_session_id'] = session_id

    chat_session, created = ChatSession.objects.get_or_create(
        session_id=session_id,
        defaults={'user': request.user if request.user.is_authenticated else None}
    )
    return chat_session


@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_msg = data.get('message', '').strip()

        if not user_msg:
            return JsonResponse({'error': 'Empty message'}, status=400)

        session = get_or_create_session(request)

        # Save user's message
        user_message = Message.objects.create(
            session=session,
            is_user=True,
            content=user_msg,
        )

        # --- Bot logic (dummy response here) ---
        bot_reply = f"Echo: {user_msg}"
        bot_message = Message.objects.create(
            session=session,
            is_user=False,
            content=bot_reply,
        )

        return JsonResponse({
            'reply': bot_message.content,
            'timestamp': bot_message.timestamp.isoformat()
        })
    return JsonResponse({'error': 'Invalid request'}, status=405)


@login_required
def dashboard(request):
    sessions = ChatSession.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'chatbot/dashboard.html', {'sessions': sessions})


@login_required
def session_detail(request, session_id):
    session = get_object_or_404(ChatSession, session_id=session_id, user=request.user)
    messages = session.messages.order_by('timestamp')
    return render(request, 'chatbot/session_detail.html', {
        'session': session,
        'messages': messages
    })


@csrf_exempt
def submit_feedback(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message_id = data.get('message_id')
        rating = int(data.get('rating', 0))
        comment = data.get('comment', '')

        message = get_object_or_404(Message, pk=message_id, is_user=False)

        Feedback.objects.create(
            message=message,
            rating=rating,
            comment=comment
        )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid request'}, status=405)
