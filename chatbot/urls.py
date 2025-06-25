from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    path('sessions/', views.session_history, name='session_history'),
    path('feedback/<int:session_id>/', views.feedback, name='feedback'),
]
