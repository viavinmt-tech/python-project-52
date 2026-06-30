from django.urls import reverse
from task_manager.tests.base import BaseTestCase

class TaskViewsTest(BaseTestCase):
    def test_tasks_list_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 302)
    
    def test_tasks_list_with_login(self):
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)
