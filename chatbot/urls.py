from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('api/chat/', views.chat_api, name='chat_api'),
    path('api/feedback/', views.submit_feedback, name='submit_feedback'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('session/<uuid:session_id>/', views.session_detail, name='session_detail'),
]
