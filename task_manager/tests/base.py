from django.test import TestCase
from django.contrib.auth.models import User

class BaseTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'  # nosonar
        )
        self.client.login(username='testuser', password='testpass123')  # nosonar
