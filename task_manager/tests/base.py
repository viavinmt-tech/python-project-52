from django.test import TestCase
from django.contrib.auth.models import User
import uuid

class BaseTestCase(TestCase):
    def setUp(self):
        test_password = str(uuid.uuid4())
        self.user = User.objects.create_user(
            username='testuser',
            password=test_password
        )
        self.client.login(username='testuser', password=test_password)
