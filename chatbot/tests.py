from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import ChatSession, ChatMessage

class ChatAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_user_registration(self):
        response = self.client.post('/register/', {
            'username': 'newuser',
            'password': 'newpass'
        })
        self.assertEqual(response.status_code, 302)  # should redirect to login
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login(self):
        response = self.client.post('/', {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 302)  # should redirect to dashboard

    def test_create_chat_session(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

        session = ChatSession.objects.create(user=self.user, title="Test Session")
        self.assertTrue(ChatSession.objects.filter(id=session.id).exists())

    def test_chat_message_saving(self):
        session = ChatSession.objects.create(user=self.user, title="Demo")
        message = ChatMessage.objects.create(session=session, role='user', content="Hello")
        self.assertEqual(message.content, "Hello")
