from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TaskViewsTest(TestCase):
    def test_tasks_list_requires_login(self):
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 302)
    
    def test_tasks_list_with_login(self):
        User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)
