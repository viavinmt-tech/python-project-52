from django.test import TestCase
from django.contrib.auth.models import User
import uuid

class UserModelTest(TestCase):
    def test_user_creation(self):
        test_password = str(uuid.uuid4())
        user = User.objects.create_user(
            username='testuser',
            password=test_password,
            first_name='Test',
            last_name='User'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
